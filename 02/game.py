#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import sys
import random
import itertools
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    letters = []
    for count in range(0, 7):
        letter = random.choice(POUCH)
        # Got a letter, need to remove it from POUCH
        for x in POUCH:
            if letter == x:
                idx = POUCH.index(x)
                del POUCH[idx]
                break
        letters.append(random.choice(POUCH))
    return letters


def get_possible_dict_words(letters):
    allwords = []
    for idx in range(1, 7):
        for item in _get_permutations_draw(letters[:-idx]):
            allwords.append(''.join(item).lower())
    res = (set(allwords).intersection(DICTIONARY))
    print(res)
    return res


def _get_permutations_draw(letters):
    return itertools.permutations(letters)


def _validation(user_word, letters):
    for letter in user_word.lower():
        if letter.lower() not in letters:
            return False
    return True


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_user_input():
    return raw_input("Enter your word: ")


def main():
    # Draw 7 letters from POUCH
    user_letters = draw_letters()
    print("Letters drawn: {}".format(' '.join(user_letters)))

    # Get user's word
    user_word = raw_input("Enter your word: ")

    while user_word not in DICTIONARY:
        print('word is invalid')
        user_word = get_user_input()

    # Verify user_word uses letters from draw
    if not _validation(user_word, user_letters):
        sys.exit("Your word uses letters you don't have")
    user_word_score = calc_word_value(user_word)
    print("Word chosen: {} (value: {})".format(user_word, user_word_score))

    # Get highest value word from letters drawn
    possible_words = get_possible_dict_words(user_letters)
    best_word = max_word_value(possible_words)
    best_word_score = calc_word_value(best_word)

    if user_word_score >= best_word_score:
        print("CONGRATS! You have the highest word score!")
        print("Best word: {} (value: {})".format(best_word, best_word_score))
    elif best_word != user_word and user_word_score == best_word_score:
        print("Another word with the same value: {} (value: {})".format(best_word.upper(), calc_word_value(best_word)))
    else:
        print("Best word is: {} (value: {})".format(best_word.upper(), best_word_score))


if __name__ == "__main__":
    main()
