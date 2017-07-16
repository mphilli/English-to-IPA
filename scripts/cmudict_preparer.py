# -*- coding: utf-8 -*-
# This script is used to prepare a source version of the CMU dict to be compatible with conversion.py
# Converts the CMU dictionary to consist of one line for each word, with multiple entries separated by a % symbol
# The newly generated file can be used to backup/update the CMU_dict.txt file in the src folder
# (By default, each unique pronunciation of a word will appear on its own line)
# SOURCE FILE FROM: http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b
# Note that the source file has been abridged (omits comments and some pronunciations regarding punctuation).

import os
import re

version = "0.7b"
unique_dict = {}
pattern = "([A-Za-z\-\._']+)\(\d\)"
print("running cmudict_preparer...")

# read info from old file
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       '..\src\\resources\CMU_source_files/cmudict-' + version + '.txt'), encoding="UTF-8") as file:
    print("reading source file...")
    for line in file.readlines():
        if line.startswith(";;;"):
            pass  # ignore comment lines, if not already removed
        else:
            word = line.split(" ")[0]
            if re.findall(pattern, word):
                unique_dict[re.findall(pattern, word)[0]] += "%" + ' '.join(line.replace("\n", "").split(" ")[1:])
            else:
                unique_dict[word] = ' '.join(line.split(" ")[1:])

# write info to new file
new_file_name = 'PREPARED-cmudict-' + version + '.txt'
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       new_file_name), "w+", encoding="UTF-8") as prepared:
    for entry in unique_dict:
        line = entry + " " + unique_dict[entry]
        prepared.write(line.replace("\n", "").replace("% ", "%").lower() + "\n")
    print(new_file_name + " created.")

