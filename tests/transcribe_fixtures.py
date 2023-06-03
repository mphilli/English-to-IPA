# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

class BaseConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_ellipsis(self):
        res1 = transcribe.get_cmu(self.words6, db_type='sql')
        res2 = transcribe.get_cmu(self.words6, db_type='json')
        self.assertEqual(res1, self.cmu6)
        self.assertEqual(res2, self.cmu6)
        self.assertEqual(res1, res2)

    def test_cmu_to_ipa_ellipsis(self):
        res1 = transcribe.cmu_to_ipa(self.cmu6, stress_marking='both')
        self.assertEqual(res1, self.ipa6)
