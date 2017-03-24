# -*- coding: utf-8 -*-
import re
"""
IPA GENERATOR 2.0
Author: Michael Phillips
Last update: 3/23/17

A simple script for converting English words into IPA notation.
The conversion relies on the CMU Phonetic Dictionary. As such, if a word entry is missing, the word is not converted
to IPA, and the original is returned. There are sometimes more than one correct pronunciations of a word, and so
this program can return either just the top result or every possible combination of results.
"""


def cmu_words():
    """returns a dictionary of words and their CMU phonetic transcriptions"""
    cmu_file = open('CMU_dict.txt', 'r+')  # assumes the file is in the same directory!
    words = []
    phonetics = []
    for line in cmu_file.readlines():
        words.append(line.split()[0])
        phonetics.append(' '.join(line.split()[1:]).split('%'))
    cmu_dict = {w: p for w, p in zip(words, phonetics)}
    return cmu_dict


def get_cmu(user_in):
    """converts the user's input to the CMU phonetics, returns a list of all entries found for each word"""
    cmu_list = []  # a list of CMU phonetic representations for the input words
    user_in = [re.sub("[:;,\.\?\"!]", "", word) for word in user_in]
    for word in user_in:
        if word in word_dict:
            # add the CMU phonetic representation(s) to the list
            cmu_list.append(word_dict[word])
        else:
            # If the word cannot be found in the CMU dictionary, we will ignore it
            cmu_list.append(['__IGNORE__' + word])
    return cmu_list


def cmu_to_ipa(cmu_list):
    """converts the CMU word lists into IPA transcriptions"""
    symbols = {"a": "ə", "ey": "e", "aa": "ɑ", "ae": "æ", "ah": "ə", "ao": "ɔ", "aw": "aʊ", "ay": "aɪ", "ch": "ʧ",
               "dh": "ð", "eh": "ɛ", "er": "ər", "hh": "h", "ih": "ɪ", "jh": "ʤ", "ng": "ŋ",  "ow": "oʊ", "oy": "ɔɪ",
               "sh": "ʃ", "th": "θ", "uh": "ʊ", "uw": "u", "zh": "ʒ", "iy": "i", "y": "j"}
    ipa_list = []  # the final list of IPA tokens to be returned
    for word_list in cmu_list:
        ipa_word_list = []  # the word list for each word
        for word in word_list:
            word = re.sub("[0-9]", "", word)  # ignore stress markings for now
            ipa_form = ''
            if word.startswith("__IGNORE__"):
                ipa_form = word.replace("__IGNORE__", "")
            else:
                for piece in word.split(" "):
                    if piece in symbols:
                        ipa_form += symbols[piece]
                    else:
                        ipa_form += piece
            ipa_word_list.append(ipa_form)
        ipa_list.append(list(set(ipa_word_list)))
    return ipa_list


def get_top(ipa_list):
    """Returns only the one result for a query. If multiple entries for words are found, only the first is used."""
    return ' '.join([[word for word in word_list][0] for word_list in ipa_list])


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
    final = [sent[:-1] for sent in list_all]
    return final


def convert(input):
    cmu_list = get_cmu(input)
    ipa_words = cmu_to_ipa(cmu_list)  # converts the CMU phonetic pronunciations to IPA notation
    ipa_final = get_top(ipa_words)  # also an option
    # ipa_final = get_all(ipa_words)
    if type(ipa_final) == list:
        print("List of possible transcriptions: ")
        for sent_num in range(len(ipa_final)):
            if len(ipa_final) > 1:
                print(str(sent_num + 1) + ". " + ipa_final[sent_num])  # print list of numbered results
            else:
                print(ipa_final[sent_num])
    else:
        print(ipa_final)

def main():
    """loops through user inputs and returns IPA notations until __quit__ is typed"""
    list_of_lines = []
    user_in = input("Input: ").lower().split(" ")
    while user_in != ['__quit__']:
        convert(user_in)
        user_in = input("Input: ").lower().split()


if __name__ == "__main__":
    word_dict = cmu_words()
    print("English to IPA 2.0")
    main()
