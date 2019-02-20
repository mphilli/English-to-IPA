import json
import re
from os.path import join, abspath, dirname


def create_json():
    """takes the prepared data and places it into the database"""
    data_dict = {}
    with open(join(abspath(dirname(__file__)), '..\eng_to_ipa\\resources\CMU_source_files/cmudict-0.7b.txt'), "r",
              encoding="UTF-8") as source_file:
        for line in source_file.readlines():
            word_token = line.split("  ")[0].lower()
            word = re.sub("\(\d\)", "", word_token)
            phonemes = line.split("  ")[1].replace("\n", "").lower()
            if word_token != word and word in data_dict:
                # already encountered, append
                data_dict[word].append(phonemes)
            else:
                data_dict[word] = [phonemes]
    json_dict = json.dumps(data_dict)
    with open(join(abspath(dirname(__file__)),  "../eng_to_ipa/resources/CMU_dict.json"), "w",
              encoding="UTF-8") as j_file:
        j_file.write(str(json_dict))


if __name__ == "__main__":
    create_json()
    # small test to verify valid database creation:
    json_file = open(join(abspath(dirname(__file__)),  "../eng_to_ipa/resources/CMU_dict.json"), encoding="UTF-8")
    json_obj = json.load(json_file)
    for key, val in json_obj.items():
        if "rose" in key:
            for v in val:
                print(key, v)
