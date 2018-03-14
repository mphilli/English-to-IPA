# Simple rhyming support. Call get_rhymes() on a word to find rhymes from the CMU dictionary.
from conversion import c, get_cmu


def remove_onset(word_in):
    phone_list = get_cmu([word_in])[0][0].split(" ")
    for i, phoneme in enumerate(phone_list):
        if "1" in phoneme:
            return ' '.join(phone_list[i:])


def get_rhymes(word):
    if " " in word:
        return [get_rhymes(w) for w in word.split(" ")]
    phones = remove_onset(word.lower())
    phones_full = get_cmu([word.lower()])[0][0]
    c.execute(f"SELECT word, phonemes FROM dictionary WHERE phonemes "
              f"LIKE \"%{phones}\" AND NOT word=\"{word}\" "  # don't count word as its own rhyme
              f"AND NOT phonemes=\"{phones_full}\"")  # don't return results that are the same but spelled differently
    return sorted(list(set([r[0] for r in c.fetchall()])))


if __name__ == "__main__":
    word = "testing"
    rhymes = get_rhymes(word)
    for rhyme in rhymes:
        print(rhyme)