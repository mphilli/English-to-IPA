# -*- coding: utf-8 -*-
from eng_to_ipa import syllables
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the syllable functions."""

    def test_count(self):
        test_string = "reflect respect recline reduce obsessively demonstrate baseball cloud brother cobblestone " + \
                      "complete conspire conflict estuary"  # Syllable counts: 2 2 2 2 4 3 2 1 2 3 2 2 2
        expected = [2, 2, 2, 2, 4, 3, 2, 1, 2, 3, 2, 2, 2, 4]
        for i, word in enumerate(test_string.split()):
            self.assertEqual(syllables.syllable_count(word), expected[i])

        # test some examples with hiatus
        test_hiatus = "duo rio maria created misery harry"  # syllable counts: 2 2 3 3 3 2
        hiatus_counts = [2, 2, 3, 3, 3, 2]
        for j, word in enumerate(test_hiatus.split()):
            self.assertEqual(syllables.syllable_count(word), hiatus_counts[j])

if __name__ == "__main__":
    unittest.main()
