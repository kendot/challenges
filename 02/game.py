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


def get_possible_dict_words(letters, user_word):
    allwords = []
    print(letters)
    for item in xrange(0, len(letters)+1):
        els = [list(words) for words in itertools.combinations(letters, item)]
        allwords.extend(els)

    v = []
    for group in allwords:
        v.append(''.join(group).lower())

    print(sorted(v))

    if user_word in v:
        print('!! FOUND USER WORD: {}'.format(user_word))
    else:
        print('!! USER WORD NOT FOUND: {}'.format(user_word))

    res = (set(v).intersection(DICTIONARY))
    print(sorted(res))
    return res


def _get_permutations_draw(letters):
    return itertools.permutations(letters)


def _validation(user_word, letters):
    for letter in user_word.lower():
        if letter.upper() not in letters:
            return False
    return True


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    # print(word)
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_user_input():
    return raw_input("Enter your word: ")


def main():
    # Draw 7 letters from POUCH
    print("-"*10)
    user_letters = draw_letters()
    print("Letters drawn: {}".format(' '.join(user_letters)))

    # Get user's word
    user_word = raw_input("Enter your word: ").lower()

    while user_word not in DICTIONARY:
        print('word is invalid')
        user_word = get_user_input()

    # Verify user_word uses letters from draw
    if not _validation(user_word, user_letters):
        sys.exit("Your word uses letters you don't have")
    user_word_score = calc_word_value(user_word)
    print("Word chosen: {} (value: {})".format(user_word, user_word_score))

    # Get highest value word from letters drawn
    possible_words = get_possible_dict_words(user_letters, user_word)
    best_word = max_word_value(possible_words)
    best_word_score = calc_word_value(best_word)

    if user_word_score >= best_word_score:
        print("CONGRATS! You have the highest word score!")
        print("Best word: {} (value: {})".format(best_word, best_word_score))
    elif user_word_score == best_word_score and best_word != user_word:
        print("Another word with the same value: {} (value: {})".format(best_word.upper(), calc_word_value(best_word)))
    else:
        print("Best word is: {} (value: {})".format(best_word.upper(), best_word_score))


if __name__ == "__main__":
    while True:
        main()
