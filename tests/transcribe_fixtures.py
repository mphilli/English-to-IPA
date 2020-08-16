# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import unittest

class BaseConversion(unittest.TestCase):
    """Simple unit testing for the transcribe function(s)."""

    def test_get_cmu_on_demand(self):
        res0 = transcribe.get_cmu(self.words0, db_type='sql')
        self.assertEqual(res0, self.cmu0)