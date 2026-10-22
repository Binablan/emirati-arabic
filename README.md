# Emirati Arabic Skill | مهارة اللهجة الإماراتية

**By Binablan · v0.2.0 source update · MIT (original project material)**

مهارة أولية تساعد المساعدات الذكية على كتابة ومراجعة العربية الإماراتية، مع قواعد محدودة موثّقة وأمثلة قابلة للمراجعة. ليست معجمًا شاملًا، ولا بديلًا عن مراجعة متحدثي اللهجة.

A small, source-grounded skill for writing and reviewing Emirati Arabic. It prioritizes preserving meaning, avoiding mechanical letter substitutions, and distinguishing source evidence from original examples.

## v0.2.0 — تخصص أبوظبي وتصحيحات صاحب المهارة

الإماراتية العامة باقية افتراضياً؛ يُفعّل تخصص أبوظبي عند طلبه فقط. أُضيف معجم محدود مع إحالة لكل مدخل، وقواعد للنطق والسياق، ومحادثات وتحويلات مؤلفة، وضوابط تمنع التصنّع، وفحوص للمعنى السطحي والتوثيق.

- [دليل أبوظبي](references/abu-dhabi.md) · [المعجم المنظّم](references/abu-dhabi-lexicon.json)
- [المعجم المقروء والمحادثات والتحويلات](references/abu-dhabi-examples.md)
- [المصادر وحدودها](references/abu-dhabi-sources.md) · [التقييم](references/evaluation.md)
- [حالات التقييم](tests/fixtures/abu_dhabi_cases.json) · [أداة الفحص](scripts/check_conversions.py)

الموثّق في مصدر عن أبوظبي ليس بالضرورة حصرياً لها. شواهد Qafisheh تاريخية، وشواهد Habash et al. موسومة بأبوظبي في دراسة كتابة ونطق؛ لا يثبت أي منهما وحده طبيعية محادثة معاصرة عند كل المتحدثين. الأمثلة تطبيقات أصلية غير معتمدة محلياً.

**GitHub source update, not a registry publication or GitHub Release.** The `main` installation URL below installs the repository state. The version number does not imply independent native-speaker certification.

### أمثلة صاحب المهارة المأذون بنشرها

[الأمثلة والسياقات والبدائل](references/owner-examples.md) · [النسخة المنظّمة](references/owner-examples.json) · [حالات تقييم المعنى والسياق](tests/fixtures/owner_context_cases.json).

نُقلت أمثلة Binablan بنفس كتابته وبإذنه، مع فصلها عن المصادر القديمة. تمثل اختياراته في السياقات المحددة، لا كل أهل أبوظبي. لا تُوحّد «مش» و«مب» آلياً، ولا تُخلط جهة الإخبار في «بخبرك» و«خبرنيه»، ولا «باجر» مع «عقب باجر» أو «ورا باجر». بدائل السؤال عن الوصول تختلف بحسب الموقف، و«من الصبح نترياك» قد تحمل عتاباً خفيفاً بحسب النبرة. الاختبارات تسمح ببدائل مؤلفة تحفظ القيود المحددة؛ ليست فرضاً لجملة واحدة أو حكماً دلالياً شاملاً.

## Install in Hermes

```sh
hermes skills install https://raw.githubusercontent.com/Binablan/emirati-arabic/main/SKILL.md
```

For a compatible agent that supports `SKILL.md`, download the repository and follow that agent's skill-installation instructions. Compatibility with every agent has not been tested.

## Usage | الاستخدام

Ask your assistant, for example:

- «استخدم مهارة emirati-arabic وراجع هالنص، بدون ما تغيّر معناه.»
- «حوّل النص إلى كلام إماراتي بسيط، بدون مبالغة أو حشو أمثال.»
- «اشرح القاعدة الموجودة في المهارة، واذكر مصدرها.»
- «استخدم تخصص أبوظبي وحوّل هالنص لمحادثة بسيطة؛ حافظ على الأسماء والوقت، ولا تضف نداءات.»

Original provisional example — not a source quotation:

> سوف أكتب لك الشرح. → بكتب لك الشرح.

The skill is guidance loaded by the assistant, not a new model, a voice, or an automatic guarantee of accent accuracy.

## Preserved v0.1.0 foundation

- Selected future, negation, and demonstrative constructions.
- A safeguard against indiscriminate ج → ي substitution.
- Meaning-preserving rewriting and restrained dialect markers.
- Source attribution, uncertainty, and private-versus-public correction handling.

## Reference and limitations

The initial reference is **«المتوصّف — أمثال وحكم من الإمارات»**, collected and researched by **عبدالله حمدان عبدالله أحمد بن دلموك**, published by **مركز حمدان بن محمد لإحياء التراث**, second edition, 2021 as stated in the examined copy.

The initial pronunciation/spelling rules were checked against images of printed pages **49 and 52**. This is not a claim that the whole book was reviewed. See [source notes](references/sources.md).

**The PDF, page images, bulk extracted text, private conversations, private calibration reference, historical review archives/logs, and local-machine files are not included.** Only the explicitly publication-authorized owner examples are added; other private preferences remain excluded. This project is independent and does not claim endorsement by the referenced authors, publishers, or Nous Research.

## Contribute | المساهمة

Corrections and additional well-supported examples are welcome. Explain the context and, where relevant, the regional variety. Separate a personal preference from a broader claim. Do not upload private conversations or copyrighted books. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Tests

From the repository directory, with Python 3.10 or later:

```sh
python -m unittest discover -s tests -v
```

These tests check structure, source metadata, publication hygiene, and the conversion checker with positive/negative authored cases. They do not prove linguistic fluency, full semantic equivalence, or universal naturalness. To check actual model outputs, use the separate workflow in [evaluation.md](references/evaluation.md); do not present reference-fixture self-tests as model evaluation.

## License

Original instructions, documentation, code, and newly authored examples are provided under the [MIT License](LICENSE), copyright Binablan. The referenced book and any third-party source material retain their own rights; this repository does not license or redistribute the book. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
