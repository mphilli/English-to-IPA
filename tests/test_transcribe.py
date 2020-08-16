# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import transcribe_fixtures
import sys

words0 = "on-demand".split()

class TestConversion_default(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.words0 = words0
        self.cmu0   = [['aa1 n d ih0 m ae1 n d', 'ao1 n d ih0 m ae1 n d']]
        self.lang   = None