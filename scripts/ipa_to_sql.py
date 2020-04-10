from eng_to_ipa import transcribe
import sqlite3
import re
from os.path import join, abspath, dirname

conn = sqlite3.connect(join(abspath(dirname(__file__)),
                            "../eng_to_ipa/resources/CMU_dict.db"))
c = conn.cursor()


def create_dictionary_table():
    try:
        c.execute("""CREATE TABLE eng_ipa
                    (id INTEGER PRIMARY KEY,
                    word text NOT NULL,
                    phonemes text NOT NULL,
                    ipa text NOT NULL
                    )""")
        conn.commit()
    except sqlite3.OperationalError:
        c.execute("DROP TABLE eng_ipa;")
        conn.commit()
        create_dictionary_table()


def insert_dictionary_values():
    """takes the prepared data and places it into the database"""
    dictionary_data = []
    with open(join(abspath(dirname(__file__)), '..\\eng_to_ipa\\resources\\CMU_source_files/cmudict-0.7b.txt'),
              encoding="UTF-8") as source_file:
        for line in source_file.readlines():
            word = re.sub(r"\(\d\)", "", line.split("  ")[0]).lower()
            phonemes = line.split("  ")[1].replace("\n", "").lower()
            ipa = transcribe.cmu_to_ipa([[phonemes]], stress_marking="both")[0][0]
            dictionary_data.append((str(word), str(phonemes), str(ipa)))
    c.executemany("INSERT INTO eng_ipa(word, phonemes, ipa) VALUES (?, ?, ?)", dictionary_data)
    conn.commit()


if __name__ == "__main__":
    # create_dictionary_table()
    # insert_dictionary_values()
    # test
    c.execute("SELECT * FROM eng_ipa WHERE "
              "REPLACE(REPLACE(ipa, 'ˌ', ''), 'ˈ', '') "
              "LIKE \"%nstr%\"")
    for r in c.fetchall():
        print(str(r))
