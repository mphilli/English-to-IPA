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

Some notes and key functions:

* The CMU_dict.txt file must be in the same directory as conversion.py in order to work! 
* Words which cannot be found in the CMU dictionary are ignored and simply reprinted. 
* Simple punctuation is stripped away (?, !, ., etc). 
* Should only take one line of input at a time
* **convert(input, retrieve)** - takes a string or list of English text and returns it as a single IPA string. If the **retrieve** parameter is set to 'ALL', a list is instead returned, with all possible combinations of discovered transcriptions returned. 
            
      convert('the quick brown fox jumped over the lazy dog')
      ðə kwɪk braʊn fɑks ʤəmpt oʊvər ðə lezi dɔg   
* **isin_cmu(word)** - checks if a given word or phrase is in the CMU phonetic dictionary. If a phrase is given, only returns true if all words are in the dictionary. 
* **get_ipa_list(input)** - returns each transcribed IPA token as a list of all discovered transcriptions. 

        get_ipa_list('The receptionists were busy')
        [['ðə', 'ði'], ['risɛpʃənɪs', 'risɛpʃənɪsts', 'rɪsɛpʃənɪs', 'rɪsɛpʃənɪsts'], ['wər'], ['bɪzi']]