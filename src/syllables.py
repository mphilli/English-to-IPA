import re
import os
import json


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'resources\phones.json'), "r") as phones_json:
    PHONES = json.load(phones_json)

# list of adjacent vowel symbols that constitute separate nuclei
hiatus = [["er", "iy"], ["iy", "ow"], ["uw", "ow"], ["iy", "ah"], ["iy", "ey"], ["uw", "eh"], ["er", "eh"]]


def count(word):
    word = re.sub("\d", "", word).split(' ')
    if "__IGNORE__" in word[0]:
        return 0
    else:
        nuclei = 0
        for i, sym in enumerate(word):
            prev_phone = PHONES[word[i-1]]
            prev_sym = word[i-1]
            if PHONES[sym] == 'vowel':
                if i > 0 and not prev_phone == 'vowel' or i == 0:
                    nuclei += 1
                elif [prev_sym, sym] in hiatus:
                    nuclei += 1
        return nuclei
