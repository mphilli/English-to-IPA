# -*- coding: utf-8 -*-
from eng_to_ipa import rhymes
import unittest

test_case_1 = [['climbing', 'diming', 'liming', 'priming', 'timing'],
               ['compunction', 'conjunction', 'dysfunction', 'injunction', 'junction', 'malfunction']]
test_case_2 = []


class TestConversion(unittest.TestCase):
    """Simple unit testing for the rhymes function(s)."""

    def test_rhymes(self):
        # with mode: sql
        self.assertEqual(rhymes.get_rhymes("rhyming function", mode='sql'), test_case_1)
        self.assertEqual(rhymes.get_rhymes("orange", mode='sql'), test_case_2)

    def test_jhymes(self):
        self.assertEqual(rhymes.jhymes("rhyming function"), test_case_1)
        self.assertEqual(rhymes.jhymes("orange"), test_case_2)


if __name__ == "__main__":
    unittest.main()
