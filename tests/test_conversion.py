# -*- coding: utf-8 -*-
import conversion
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the conversion script."""

    def test_preprocess(self):
        """Test preprocess function"""
        self.assertEqual(conversion.preprocess('This is a test phrase.'), 'this is a test phrase')
        self.assertEqual(conversion.preprocess('That\'s a new hat, no?'), 'that\'s a new hat no')
        self.assertEqual(conversion.preprocess('I can\'t believe she spent £50.00!'),
                         'i can\'t believe she spent £50.00')

    def test_get_cmu(self):
        self.assertEqual(conversion.get_cmu(['i', 'love', 'you']), [['ay1'], ['l ah1 v'], ['y uw1']])
        # test that __IGNORE__ is working as intended
        self.assertEqual(conversion.get_cmu(['i', 'love', 'that', 'emoji']),
                         [['ay1'], ['l ah1 v'], ['dh ae1 t', 'dh ah0 t'], ['__IGNORE__emoji']])

    def test_cmu_to_ipa(self):
        # continue using results from previous test method
        self.assertEqual(conversion.cmu_to_ipa([['ay1'], ['l ah1 v'], ['y uw1']]), [['aɪ'], ['ləv'], ['ju']])
        self.assertEqual(conversion.cmu_to_ipa([['ay1'], ['l ah1 v'], ['dh ae1 t'], ['__IGNORE__emoji']]),
                         [['aɪ'], ['ləv'], ['ðæt'], ['emoji*']])
        # test mark parameter
        self.assertEqual(conversion.cmu_to_ipa([['ay1'], ['l ah1 v'], ['dh ae1 t'], ['__IGNORE__emoji']],
                                               mark=False),
                         [['aɪ'], ['ləv'], ['ðæt'], ['emoji']])  # remove asterisk

    def test_isin_cmu(self):
        """Test efficacy of boolean retriever"""
        # test on a single word
        self.assertEqual(conversion.isin_cmu('hello'), True)
        self.assertEqual(conversion.isin_cmu('hlleo'), False)
        # test on a phrase
        self.assertEqual(conversion.isin_cmu('This is a test phrase.'), True)
        # if one word is spelled wrong, return False
        self.assertEqual(conversion.isin_cmu('Sentence spelled wrong is sentents'), False)

    def test_cmu_words(self):
        """This test should fail if the size of unique entries in the CMU dictionary changes."""
        self.assertEqual(len(conversion.cmu_words()), 125000)

    def test_ipa_list(self):
        self.assertEqual(conversion.ipa_list('This is a test phrase.'), [['ðɪs'], ['ɪz'], ['e'], ['tɛst'], ['frez']])
        # test on example sentence from README
        self.assertEqual(conversion.ipa_list('The receptionists were busy.'),
                         [['ði', 'ðə'], ['riˈsɛpʃənɪs', 'riˈsɛpʃənɪsts',
                                         'rɪˈsɛpʃənɪs', 'rɪˈsɛpʃənɪsts'], ['wər'], ['ˈbɪzi']])

    def test_convert(self):
        # example from the README:
        self.assertEqual(conversion.convert('The quick brown fox jumped over the lazy dog.'),
                         'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈlezi dɔg')
        # test same with retrieve=ALL, should return a list
        # this also tests the efficacy of the get_all() algorithm
        self.assertEqual(conversion.convert('The quick brown fox jumped over the lazy dog.', retrieve='ALL'),
                         ['ði kwɪk braʊn fɑks ʤəmpt ˈoʊvər ði ˈlezi dɔg',
                          'ði kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈlezi dɔg',
                          'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ði ˈlezi dɔg',
                          'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈlezi dɔg'])

if __name__ == "__main__":
    unittest.main()
