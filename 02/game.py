#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    start = len(POUCH)
    letters = []
    for count in range(0, 7):
        letter = random.choice(POUCH)
        print('Letter: {}'.format(letter))
        # Got a letter, need to remove from POUCH
        for x in POUCH:
            if letter == x:
                print('Found Letter: {}'.format(x))
                idx = POUCH.index(x)
                del POUCH[idx]
                break
        letters.append(random.choice(POUCH))
    print(start)
    print(len(POUCH))

    return letters


def get_possible_dict_words():
    pass


def _get_permutations_draw():
    pass


def _validation():
    pass


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    print(draw_letters())
    # print(DICTIONARY)


if __name__ == "__main__":
    main()
