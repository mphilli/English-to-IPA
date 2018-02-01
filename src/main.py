# -*- coding: utf-8 -*-
# A basic command line interface for calling the conversion function
# If you want to keep punctuation in the result, set keep_punct=True
# If you want to get all possible IPA transcriptions, set retrieve_all=True
# Currently, keep_punct=True only returns one result (not all)
import conversion


def main():
    """loops through user inputs and returns IPA notations until __quit__ is typed"""
    user_in = input("Input: ").lower()
    while user_in != [''] and user_in != ['__quit__']:
        ipa = conversion.convert(user_in, retrieve_all=True, keep_punct=True)
        if type(ipa) == list:  # if retrieve=ALL
            if len(ipa) > 1:
                print("List of possible transcriptions: ")
                for sent_num in range(len(ipa)):
                    print(str(sent_num + 1) + ". " + ipa[sent_num])  # print list of numbered results
            else:
                print(ipa[0])  # when ALL is used but there's only one result
        else:
            print(ipa)
        user_in = input("Input: ").lower().split(" ")


if __name__ == "__main__":
    print("English to IPA")
    main()

"""
7/16/2017
TODO:

* Allow a retrieve_all for IPA with preserved punctuation
* Continue to improve and debug stress marking and syllable recognition
* Preserve the capitalization and punctuation of unrecognized tokens (?)
* Add logging and exception handling to functions
"""
