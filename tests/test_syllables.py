# -*- coding: utf-8 -*-
import conversion
import syllables
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the syllable functions."""

    def test_count(self):
        test_string = "reflect respect recline reduce obsessively demonstrate baseball cloud brother cobblestone " + \
                      "complete conspire conflict estuary"  # Syllable counts: 2 2 2 2 4 3 2 1 2 3 2 2 2
        raw_cmu = conversion.get_cmu(test_string.split(" "))
        expected = [2, 2, 2, 2, 4, 3, 2, 1, 2, 3, 2, 2, 2, 4]
        for i, word in enumerate(raw_cmu):
            self.assertEqual(syllables.count(word[0]), expected[i])

        # test some examples with hiatus
        test_hiatus = "duo rio maria created misery harry"  # syllable counts: 2 2 3 3 3 2
        hiatus_counts = [2, 2, 3, 3, 3, 2]

        raw_cmu_hiatus = conversion.get_cmu(test_hiatus.split(" "))
        for j, word in enumerate(raw_cmu_hiatus):
            self.assertEqual(syllables.count(word[0]), hiatus_counts[j])

if __name__ == "__main__":
    unittest.main()
