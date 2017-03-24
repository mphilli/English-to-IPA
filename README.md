# IPA Generator 2.0 (Python 3) 
Converts English text to IPA notation

I noticed some people were making use of my first IPA program, so I decided to write a better version. This program utilizes the Carnegie-Mellon University Phonetic Dictionary Database to convert English words into IPA. 


    English to IPA 2.0
    Word or Phrase: unnaturally
    List of possible transcriptions: 
    1. ənnæʧərəli
    2. ənnæʧərli
    3. ənæʧərli
    4. ənnæʧrəli

The get_all function returns all transcriptions given the possible combinations thereof, and the get_top function returns only the first result. 

Some notes:

* The CMU_dict.txt file must be in the same directory as conversion.py in order to work! 
* Words which cannot be found in the CMU dictionary are ignored and simply reprinted. 
* Simple punctuation is stripped away (?, !, ., etc). 
* Should only take one line of input at a time
