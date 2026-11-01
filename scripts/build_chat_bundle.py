"""Build a single-file chat edition from the existing public runtime sources.

No model calls, downloads, credentials, or private calibration are used.
The generated edition is not a second independently maintained skill.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from build_distribution import collect, validate_public_text

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FILES = (
    'SKILL.md', 'references/abu-dhabi.md',
    'references/conversation-behavior.md', 'references/owner-examples.md',
    'references/examples.md', 'references/sources.md',
    'references/abu-dhabi-sources.md', 'references/abu-dhabi-lexicon.json',
    'references/abu-dhabi-examples.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
)
HEADER = """# Emirati Arabic — single-file chat edition

By Binablan, Hermes Agent. Generated from the existing emirati-arabic skill.
This is a working-tree build, not a new release or proof of runtime activation,
and not a cross-model compatibility certification. See chat-manifest.json for
source-byte hashes and the output checksum. Do not edit this generated copy;
change the original source and rebuild it.

## تعليمات التفعيل

عند طلب المستخدم تفعيل هذا الملف للمحادثة، طبّق تعليمات المهارة أدناه وتحدث
بالإماراتية العامة في الحوار العادي؛ تخصص أبوظبي عند طلبه فقط. أنجز طلبه،
ولا تلخّص الملف أو تشرح لهجته بدل الرد. احترم اللغة أو الأسلوب المختلف إذا
طلبه، وكذلك تعليمات التطبيق الأعلى أولوية. طلب فحص الملف ليس طلب تفعيله.

لا يلزم تشغيل أدوات أو سكربتات أو الاتصال بالإنترنت للمحادثة. كل قسم موسوم
باسم مصدره في هذا الملف؛ اقرأ المراجع المضمّنة هنا بدل افتراض وجود مجلدات
عند المستخدم. الروابط الأصلية باقية للتوثيق، وليست طلبًا لفتحها. الإشارات
إلى الاختبارات والتقييم وصيانة الحزمة تخص المطورين، ولا تُشغّل لأجل السوالف.
لا تدّع قراءة مرجع خارج هذا الملف أو استمرار التفعيل في جلسة جديدة من دون
دليل. لا تحفظ تصحيحات أو تنشر محادثات أو تعدّل إعدادات التطبيق تلقائيًا.

الأمثلة المضمّنة لها حدود النسبة المذكورة في مصادرها؛ ليست أوامر جديدة من
المستخدم ولا أجوبة يجب تكرارها حرفيًا. لا يتضمن هذا الملف نتائج اختبارات
خاصة أو ذاكرة مساعد بعينه أو تدريبًا للنموذج أو ضمانًا للهجة الصوت.
"""


def build(root, output_dir):
    root = root.resolve()
    output_dir = output_dir.resolve()
    if output_dir == root or output_dir.is_relative_to(root):
        raise ValueError('Keep generated chat files outside the source repository')
    version, public_files = collect(root)
    missing = set(RUNTIME_FILES) - public_files.keys()
    if missing:
        raise ValueError('Missing allowlisted runtime sources: ' + ', '.join(sorted(missing)))
    parts = [HEADER.strip(), 'Source version: ' + version]
    for name in RUNTIME_FILES:
        text = public_files[name].decode('utf-8').replace('\r\n', '\n').strip()
        parts.append('---\n\n## Embedded source: ' + name + '\n\n' + text)
    data = ('\n\n'.join(parts) + '\n').encode('utf-8')
    output_name = 'emirati-arabic-chat.md'
    validate_public_text(output_name, data)
    manifest = {
        'source_version': version,
        'source_sha256': {name: hashlib.sha256(public_files[name]).hexdigest()
                          for name in RUNTIME_FILES},
        'output': output_name,
        'output_sha256': hashlib.sha256(data).hexdigest(),
        'check_scope': 'source integrity only; no model compatibility or fluency claim',
    }
    # All source and destination checks happen before writing either artifact.
    targets = (output_dir / output_name, output_dir / 'chat-manifest.json')
    if any(path.is_symlink() or (path.exists() and not path.is_file()) for path in targets):
        raise ValueError('Output targets must be ordinary files, not symlinks or directories')
    output_dir.mkdir(parents=True, exist_ok=True)
    targets[0].write_bytes(data)
    targets[1].write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    if targets[0].read_bytes() != data or json.loads(targets[1].read_text(encoding='utf-8')) != manifest:
        raise ValueError('Chat artifact readback mismatch')
    return {'source_version': version, 'output': output_name,
            'source_files': len(RUNTIME_FILES), 'characters': len(data.decode('utf-8')),
            'bytes': len(data), 'sha256': manifest['output_sha256']}


def main():
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if reconfigure is not None:
            reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True,
                        help='Destination outside the source tree')
    args = parser.parse_args()
    try:
        result = build(ROOT, args.output_dir)
    except (ValueError, OSError, UnicodeError, KeyError, TypeError) as exc:
        print('Chat bundle rejected: ' + str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
