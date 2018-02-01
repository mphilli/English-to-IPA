# -*- coding: utf-8 -*-
import re
import os
import stress

"""
IPA GENERATOR
Author: Michael G. Phillips
Last update: 7/16/2017

A simple script for converting English words into IPA notation (American English).
The conversion relies on the CMU Phonetic Dictionary. As such, if a word entry is missing, the word is not converted
to IPA, and the original is returned. There is sometimes more than one correct pronunciation of a word, and so
we can return either just the top result or every possible combination of results.
"""


def cmu_words():
    """returns a dictionary of words from the CMU dictionary and their phonetic notation"""
    cmu_file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),  'resources\CMU_dict.txt'), 'r+')
    words = []
    phonetics = []
    for line in cmu_file.readlines():
        words.append(line.split()[0])
        phonetics.append(' '.join(line.split()[1:]).split('%'))
    cmu_dict = {w: p for w, p in zip(words, phonetics)}
    cmu_file.close()
    return cmu_dict

word_dict = cmu_words()


def preprocess(words):
    """Returns a string of words stripped of punctuation"""
    punct_str = '!"#$%&\'()*+,-./:;<=>/?@[\\]^_`{|}~«» '
    return ' '.join([w.strip(punct_str).lower() for w in words.split()])


def preserve_punc(words):
    """converts words to IPA and finds punctuation before and after the word."""
    words_preserved = []
    for w in words.split():
        punct_list = ["", preprocess(w), ""]
        before = re.search("^([^A-Za-z0-9]+)[A-Za-z]", w)
        after = re.search("[A-Za-z]([^A-Za-z0-9]+)$", w)
        if before:
            punct_list[0] = str(before.group(1))
        if after:
            punct_list[2] = str(after.group(1))
        words_preserved.append(punct_list)
    return words_preserved


def punct_ipa(str_in):
    """takes a string of text and returns as IPA, with punctuation preserved"""
    pres_ipa = preserve_punc(str_in)
    for i, comb in enumerate(pres_ipa):
        _cmu = get_cmu([comb[1]])
        _ipa = cmu_to_ipa(_cmu)
        _result = get_top(_ipa)
        pres_ipa[i][1] = _result
    return ''.join([''.join([w for w in word]) + " "
                    for word in pres_ipa])


def get_cmu(user_in):
    """converts the user's input to the CMU phonetics, returns a list of all entries found for each word"""
    cmu_list = []  # a list of CMU phonetic representations for the input words

    for word in user_in:
        if word in word_dict:
            # add the CMU phonetic representation(s) to the list
            cmu_list.append(word_dict[word])
        else:
            # If the word cannot be found in the CMU dictionary, we will ignore it
            cmu_list.append(['__IGNORE__' + word])
    return cmu_list


def cmu_to_ipa(cmu_list, mark=True, stress_marking=True):
    """converts the CMU word lists into IPA transcriptions"""
    symbols = {"a": "ə", "ey": "e", "aa": "ɑ", "ae": "æ", "ah": "ə", "ao": "ɔ", "aw": "aʊ", "ay": "aɪ", "ch": "ʧ",
               "dh": "ð", "eh": "ɛ", "er": "ər", "hh": "h", "ih": "ɪ", "jh": "ʤ", "ng": "ŋ",  "ow": "oʊ", "oy": "ɔɪ",
               "sh": "ʃ", "th": "θ", "uh": "ʊ", "uw": "u", "zh": "ʒ", "iy": "i", "y": "j"}
    ipa_list = []  # the final list of IPA tokens to be returned
    for word_list in cmu_list:
        ipa_word_list = []  # the word list for each word
        for word in word_list:
            if stress_marking:
                word = stress.find_stress(word)
            else:
                if re.sub("\d*", "", word.replace("__IGNORE__", "")) == "":
                    pass  # do not delete token if it's all numbers
                else:
                    #  word = re.sub("[0-9]", "", word)
                    pass
            ipa_form = ''
            if word.startswith("__IGNORE__"):
                ipa_form = word.replace("__IGNORE__", "")
                # mark words we couldn't transliterate with an asterisk:

                if mark:
                    if not re.sub("\d*", "", ipa_form) == "":
                        ipa_form += "*"
            else:
                for piece in word.split(" "):
                    marked = False
                    unmarked = piece
                    if piece[0] in ["ˈ", "ˌ"]:
                        marked = True
                        mark = piece[0]
                        unmarked = piece[1:]
                    if unmarked in symbols:
                        if marked:
                            ipa_form += mark + symbols[unmarked]
                        else:
                            ipa_form += symbols[unmarked]

                    else:
                        ipa_form += piece
            swap_list = [["ˈər", "əˈr"], ["ˈie", "iˈe"]]
            for sym in swap_list:
                if not ipa_form.startswith(sym[0]):
                    ipa_form = ipa_form.replace(sym[0], sym[1])
            ipa_word_list.append(ipa_form)
        ipa_list.append(sorted(list(set(ipa_word_list))))
    return ipa_list


def get_top(ipa_list):
    """Returns only the one result for a query. If multiple entries for words are found, only the first is used."""
    return ' '.join([word_list[-1] for word_list in ipa_list])


def get_all(ipa_list):
    """utilizes an algorithm to discover and return all possible combinations of IPA transcriptions"""
    final_size = 1

    for word_list in ipa_list:
        final_size *= len(word_list)
    list_all = ["" for s in range(final_size)]

    for i in range(len(ipa_list)):
        if i == 0:
            swtich_rate = final_size / len(ipa_list[i])
        else:
            swtich_rate /= len(ipa_list[i])
        k = 0
        for j in range(final_size):
            if (j+1) % int(swtich_rate) == 0:
                k += 1
            if k == len(ipa_list[i]):
                k = 0
            list_all[j] = list_all[j] + ipa_list[i][k] + " "

    return sorted([sent[:-1] for sent in list_all])


def ipa_list(words_in):
    """Returns a list of all the discovered IPA transcriptions for each word."""
    if type(words_in) == str:
        words_in = [preprocess(w) for w in words_in.split(' ')]
    else:
        words_in = [preprocess(w) for w in words_in]
    cmu_list = get_cmu(words_in)
    ipa_words = cmu_to_ipa(cmu_list)
    return ipa_words


def isin_cmu(word):
    """checks if a word is in the CMU dictionary. Doesn't strip punctuation.
    If given more than one word, returns True only if all words are present."""
    word_dict = cmu_words()
    if type(word) == list or len(word.split(" ")) > 1:
        if type(word) == str:
            word = [preprocess(w) for w in word.split(' ')]
        else:
            word = [preprocess(w) for w in word]
        for w in word:
            if w.lower() not in word_dict:
                return False
        return True
    return word.lower() in word_dict


def convert(user_in, retrieve_all=False, keep_punct=False):
    """takes either a string or list of English words and converts them to IPA"""
    if keep_punct and type(user_in) == str:
        return punct_ipa(user_in)
    else:
        if type(user_in) == str:
            user_in = [preprocess(w) for w in user_in.split(' ')]
        elif type(user_in == list):
            user_in = [preprocess(w) for w in user_in]
        if '' in user_in:  # strip inputs "*" tokens
            user_in.remove('')

        cmu_list = get_cmu(user_in)
        ipa_words = cmu_to_ipa(cmu_list)  # converts the CMU phonetic pronunciations to IPA notation
        if retrieve_all:
            ipa_final = get_all(ipa_words)  # also an option
        else:
            ipa_final = get_top(ipa_words)  # gets top by default
        return ipa_final

if __name__ == "__main__":
    os.system('python main.py')  # execute main.py script

