def calculate_score(word):
    word = word.upper()

    base_score = len(word) * 10

    bonus_letters = sum(15 for l in word if l in {"X","Y","Z"})

    length_bonus = 0
    if len(word) >= 6:
        length_bonus = 20

    return base_score + bonus_letters + length_bonus