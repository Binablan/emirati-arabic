"""Portable artifact/activation checks only, not cross-model evaluation."""
import hashlib
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FILES = (
    'SKILL.md', 'references/abu-dhabi.md',
    'references/conversation-behavior.md', 'references/owner-examples.md',
    'references/examples.md', 'references/sources.md',
    'references/abu-dhabi-sources.md', 'references/abu-dhabi-lexicon.json',
    'references/abu-dhabi-examples.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
)


class PortabilityTests(unittest.TestCase):
    def copy_source(self, target):
        names = json.loads((ROOT / 'distribution-files.json').read_text(encoding='utf-8'))['files']
        for name in names:
            dest = target / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)
        return names

    def run_builder(self, source, output):
        return subprocess.run(
            [sys.executable, '-B', str(source / 'scripts/build_chat_bundle.py'),
             '--output-dir', str(output)], capture_output=True, text=True, encoding='utf-8')

    def test_missing_unlisted_or_private_runtime_rejected_before_writes(self):
        for mutation in ('missing', 'unlisted', 'private'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                source, output = Path(tmp) / 'source', Path(tmp) / 'output'
                names = self.copy_source(source)
                name = 'references/abu-dhabi.md'
                if mutation == 'missing':
                    (source / name).unlink()
                elif mutation == 'unlisted':
                    (source / 'distribution-files.json').write_text(
                        json.dumps({'files': [n for n in names if n != name]}), encoding='utf-8')
                else:
                    with (source / name).open('a', encoding='utf-8') as stream:
                        stream.write('\ngh' + 'p_' + 'x' * 30)
                result = self.run_builder(source, output)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('Chat bundle rejected:', result.stderr)
                self.assertFalse(output.exists())

    def test_in_tree_and_non_regular_output_targets_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'source'
            self.copy_source(source)
            inside = source / 'generated'
            result = self.run_builder(source, inside)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertFalse(inside.exists())
            output = Path(tmp) / 'output'
            (output / 'emirati-arabic-chat.md').mkdir(parents=True)
            result = self.run_builder(source, output)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertFalse((output / 'chat-manifest.json').exists())

    def test_unlisted_private_notes_are_not_read_or_exported(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / 'source', Path(tmp) / 'output'
            self.copy_source(source)
            private = source / 'private'
            private.mkdir()
            marker = 'PRIVATE-NOTE-NOT-FOR-EXPORT'
            (private / 'calibration.md').write_text(marker, encoding='utf-8')
            result = self.run_builder(source, output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn(marker, (output / 'emirati-arabic-chat.md').read_text(encoding='utf-8'))

    def test_usage_guide_and_builder_are_in_public_source_package(self):
        names = json.loads((ROOT / 'distribution-files.json').read_text(encoding='utf-8'))['files']
        for name in ('USAGE.md', 'scripts/build_chat_bundle.py', 'tests/test_portability.py'):
            self.assertIn(name, names)
        self.assertIn('(USAGE.md)', (ROOT / 'README.md').read_text(encoding='utf-8'))

    def test_real_cli_builds_reproducible_self_contained_runtime_bundle(self):
        script = ROOT / 'scripts/build_chat_bundle.py'
        self.assertTrue(script.is_file(), 'Portable chat builder is missing')
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            command = [sys.executable, '-B', str(script), '--output-dir', str(output)]
            env = dict(os.environ, PYTHONUTF8='0', PYTHONIOENCODING='cp1252')
            first = subprocess.run(command, capture_output=True, env=env)
            self.assertEqual(first.returncode, 0, first.stderr.decode('utf-8'))
            report = json.loads(first.stdout.decode('utf-8'))
            self.assertEqual(report['source_version'], '0.2.1-rc.1')
            self.assertEqual(report['output'], 'emirati-arabic-chat.md')
            data = (output / report['output']).read_bytes()
            text = data.decode('utf-8')
            manifest = json.loads((output / 'chat-manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(set(manifest['source_sha256']), set(RUNTIME_FILES))
            for name in RUNTIME_FILES:
                self.assertIn((ROOT / name).read_text(encoding='utf-8').strip(), text)
                self.assertEqual(manifest['source_sha256'][name],
                                 hashlib.sha256((ROOT / name).read_bytes()).hexdigest())
            self.assertEqual(manifest['output_sha256'], hashlib.sha256(data).hexdigest())
            self.assertIn('تعليمات التفعيل', text)
            self.assertIn('لا يلزم تشغيل أدوات أو سكربتات', text)
            self.assertIn('not a cross-model compatibility certification', text)
            self.assertNotIn('accepted_probes', text)
            self.assertNotIn('class BehaviorContractTests', text)
            self.assertNotIn('حالات الاختبار المحجوبة: نتائج', text)
            second = subprocess.run(command, capture_output=True, env=env)
            self.assertEqual(second.returncode, 0, second.stderr.decode('utf-8'))
            self.assertEqual(data, (output / report['output']).read_bytes())
            self.assertEqual(manifest, json.loads((output / 'chat-manifest.json').read_text(encoding='utf-8')))


if __name__ == '__main__':
    unittest.main()
