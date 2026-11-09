"""Small source-fact pilot: metadata and packaging, not dialect-fluency tests."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]

class HeritageContextTests(unittest.TestCase):
    def test_curated_reference_has_locators_and_evidence_boundaries(self):
        path=ROOT/'references/heritage-lexicon.json'
        self.assertTrue(path.is_file(), 'Curated heritage reference is missing')
        data=json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['schema_version'],1)
        self.assertEqual(data['entry_count'],8)
        self.assertEqual(len(data['entries']),data['entry_count'])
        self.assertEqual(len({e['id'] for e in data['entries']}),data['entry_count'])
        sources={s['id']:s for s in data['sources']}
        for entry in data['entries']:
            with self.subTest(entry=entry['id']):
                self.assertEqual(entry['evidence_status'],'source-attested-not-contemporary-validated')
                self.assertIn('انسب التعريف إلى المرجع', entry.get('definition_policy', ''))
                self.assertIn('المتابعة', entry['definition_policy'])
                self.assertIn('المسودات العملية', entry['definition_policy'])
                self.assertIn(entry['source_id'],sources)
                self.assertEqual(sources[entry['source_id']]['volume'],2)
                for key in ('source_form','domain','context_cues','limits'):
                    self.assertTrue(entry[key])
                for key in ('pdf_page','printed_page'):
                    self.assertIs(type(entry['locator'][key]),int)
                    self.assertGreater(entry['locator'][key],0)
                self.assertTrue(entry['senses'])
                self.assertEqual(entry['example']['status'],'original-provisional-not-owner-quotation')
                self.assertTrue(entry['example']['text'])
        forms={e['id']:e for e in data['entries']}
        self.assertEqual(len(forms['yamda']['senses']),2)
        self.assertEqual(forms['razm']['locator'],{'pdf_page':182,'printed_page':184})

    def test_optional_reference_is_wired_without_forced_heritage_usage(self):
        skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/heritage-context.md',skill)
        self.assertIn('references/heritage-lexicon.json',skill)
        self.assertIn('do not override an ordinary meaning',skill)
        self.assertIn('not a prerequisite for ordinary conversation',skill)
        guide=(ROOT/'references/heritage-context.md').read_text(encoding='utf-8')
        for boundary in ('source-attested-not-contemporary-validated', 'غير متاح', 'لا تحشر', 'حقوق'):
            self.assertIn(boundary,guide)
        self.assertIn('موسوعة الإمارات البرية',(ROOT/'THIRD_PARTY_NOTICES.md').read_text(encoding='utf-8'))

    def test_source_scope_survives_followups_without_bibliography_overload(self):
        skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        guide=(ROOT/'references/heritage-context.md').read_text(encoding='utf-8')
        for phrase in ('Carry source scope across follow-up turns',
                       'your earlier explanation is not new evidence',
                       'brief source qualifier', 'full citation only when requested'):
            self.assertTrue(phrase in skill, phrase)
        for phrase in ('شرحك السابق ليس دليلًا جديدًا', 'بحسب المرجع',
                       'لا تكرر قائمة المصادر', 'تاريخ صنع القطعة'):
            self.assertTrue(phrase in guide, phrase)

    def test_stable_identity_preserves_evidence_limits(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        notes=(ROOT/'RELEASE_NOTES.md').read_text(encoding='utf-8')
        data=json.loads((ROOT/'references/heritage-lexicon.json').read_text(encoding='utf-8'))
        self.assertTrue('v1.0.0 · Stable' in readme)
        self.assertTrue(notes.startswith('# 1.0.0 — Stable'))
        self.assertEqual(data['status'],'curated-source-reference')
        self.assertTrue('does not mean 100% accuracy' in notes)
        self.assertTrue('requires separate approval' in notes)

if __name__=='__main__': unittest.main()
