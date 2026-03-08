import os


def load_words():
    print("calling load_words()")

    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, "words.txt")

    print("loading from:", filepath)

    with open(filepath, encoding="utf-8") as f:
        words = set(
            word.strip().upper()
            for word in f
            if word.strip()
        )

    print("loaded:", len(words))
    return words

def load_words(filename="core/words.txt"):
    with open(filename) as f:
        return set(word.strip().upper() for word in f)

def is_valid_word(word, word_set):
    return word.upper() in word_set