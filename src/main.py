import conversion
"""A little interface for interacting with the convert function"""


def main():
    """loops through user inputs and returns IPA notations until __quit__ is typed"""
    user_in = input("Input: ").lower().split(" ")
    while user_in != [''] and user_in != ['__quit__']:
        ipa = conversion.convert(user_in, retrieve='TOP')
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
