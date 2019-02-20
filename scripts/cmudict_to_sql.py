# Script for converting the dictionary text file to an SQL table
import sqlite3
import re
from os.path import join, abspath, dirname

conn = sqlite3.connect(join(abspath(dirname(__file__)), "../eng_to_ipa/resources/CMU_dict.db"))
c = conn.cursor()


def create_dictionary_table():
    try:
        c.execute("""CREATE TABLE dictionary 
                    (id INTEGER PRIMARY KEY,
                    word text NOT NULL,
                    phonemes text NOT NULL
                    )""")
        conn.commit()
    except sqlite3.OperationalError:
        c.execute("DROP TABLE dictionary;")
        conn.commit()
        create_dictionary_table()


def insert_dictionary_values():
    """takes the prepared data and places it into the database"""
    dictionary_data = []
    with open(join(abspath(dirname(__file__)), '..\eng_to_ipa\\resources\CMU_source_files/cmudict-0.7b.txt'),
              encoding="UTF-8") as source_file:
        for line in source_file.readlines():
            word = re.sub("\(\d\)", "", line.split("  ")[0]).lower()
            phonemes = line.split("  ")[1].replace("\n", "").lower()
            dictionary_data.append((word, phonemes))
    c.executemany("insert into dictionary(word, phonemes) values (?, ?)", dictionary_data)
    conn.commit()


if __name__ == "__main__":
    create_dictionary_table()
    insert_dictionary_values()
    # small test to verify valid database creation:
    c.execute("SELECT * FROM dictionary WHERE word like \"%the%\"")
    for r in c.fetchall():
        print(str(r))
