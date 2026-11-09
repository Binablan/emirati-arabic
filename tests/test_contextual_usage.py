"""Context-reference integrity checks; not a dialect-fluency benchmark."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REF = 'references/contextual-usage.md'

class ContextualUsageTests(unittest.TestCase):
    def test_context_reference_preserves_corrections_and_evidence_scope(self):
        path = ROOT / REF
        self.assertTrue(path.is_file(), 'Contextual usage reference is missing')
        text = path.read_text(encoding='utf-8')
        self.assertIn('| الامور في الروب | الأمور طيبة |', text)
        self.assertIn('| المسيد العود | المسجد الكبير |', text)
        for video in ('oe14FZcDa-k', 'IXBowzBTFMs', 'jwEN7mC5ZmU'):
            self.assertIn('https://www.youtube.com/watch?v=' + video, text)
        for marker in ('Audio review: not performed', 'Exact quote timestamps: unavailable',
                       'ليست تعريفات معتمدة', 'لا تفرض', 'لا تُستنتج منها قواعد نطق'):
            self.assertIn(marker, text)

    def test_context_reference_is_loaded_and_packaged(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        names = json.loads((ROOT / 'distribution-files.json').read_text(encoding='utf-8'))['files']
        self.assertIn(REF, skill)
        self.assertIn('الامور في الروب', skill)
        self.assertIn('contextual-usage-1', skill)
        self.assertIn(REF, names)
        self.assertIn('tests/test_contextual_usage.py', names)
        self.assertIn(REF, (ROOT / 'scripts/build_chat_bundle.py').read_text(encoding='utf-8'))

if __name__ == '__main__':
    unittest.main()
