# -*- coding: utf-8 -*-

# USAGE:
# PYTHONPATH=".." python test_transcribe.py 

from eng_to_ipa import transcribe
import transcribe_fixtures
import sys

words6 = "diction… …rocks"
words6 = [transcribe.preserve_punc(w.lower())[0] for w in words6.split()]
words6 = [w[1] for w in words6]

ipa6     = [['ˈdɪkʃən'], ['rɑks']]

class TestConversion_default(transcribe_fixtures.BaseConversion):
    @classmethod
    def setUpClass(self):
        self.words6 = words6
        self.ipa6   = ipa6
        self.cmu6   = [['d ih1 k sh ah0 n'], ['r aa1 k s']]
