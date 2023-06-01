# -*- coding: utf-8 -*-
from eng_to_ipa import transcribe
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the rhymes function(s)."""

    def test_schwa(self):
        # with mode: sql
        for i in range(0, 10):
            self.assertEqual(transcribe.convert("The cup of butter caused a problem and now we're upset."),
                             "ðə kʌp ʌv ˈbʌtər kɑzd ə ˈprɑbləm ənd naʊ wir əpˈsɛt.")


if __name__ == "__main__":
    unittest.main()
