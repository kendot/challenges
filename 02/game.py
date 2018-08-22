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
    for count in range(1, 8):
        letter = random.choice(POUCH)
        # Got a letter, need to remove it from POUCH so same letter is not drawn 2x
        for x in POUCH:
            if letter == x:
                idx = POUCH.index(x)
                del POUCH[idx]
                break
        letters.append(random.choice(POUCH))

    # Check if drawn letters are only vowels, redraw if so
    if _all_vowels(letters):
        print('Only vowels, repicking...')
        draw_letters()
    print("Letters drawn: {}".format(' '.join(letters)))
    return letters


def _all_vowels(letters):
    all_vowels = {}
    for idx in range(len(letters)):
        if letters[idx] in 'AEIOU':
            all_vowels[idx] = True
        else:
            all_vowels[idx] = False
    return False if False in all_vowels.values() else True


def get_possible_dict_words(letters):
    # Iterate through all words from drawn letters then make lower case and add to list
    lower_words = []
    for group in _get_permutations_draw(letters):
        lower_words.append(''.join(group).lower())

    # Find the words common to both lists
    res = (set(lower_words).intersection(DICTIONARY))
    return res


def _get_permutations_draw(letters):
    all_words = []
    # This loop returns a list of all the possible permutations of drawn letters
    for item in range(1, len(letters)+1):
        els = [list(words) for words in itertools.permutations(letters, item)]
        all_words.extend(els)
    return all_words


def _letter_validation(user_word, letters):
    # Converts user_word to lower case then verifies word only contains letters from letters drawn
    for letter in user_word:
        if letter.upper() not in letters:
            raise ValueError
    return True


def _validation(user_word, letters):
    if user_word not in get_possible_dict_words(letters):
            raise ValueError
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
    return input("Enter your word: ")


def main():
    # Draw 7 letters from POUCH
    print("-"*10)
    user_letters = draw_letters()

    # Get user's word
    user_word = get_user_input()

    # Verify user_word uses letters from draw
    try:
        _validation(user_word, user_letters)
    except ValueError:
        print("Your word uses letters you don't have")
        user_word = get_user_input()

    user_word_score = calc_word_value(user_word)
    print("Word chosen: {} (value: {})".format(user_word, user_word_score))

    # Get highest value word from letters drawn
    possible_words = get_possible_dict_words(user_letters)
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
    play = 'y'
    while play == 'y':
        main()
        play = input("Play again? (Y/N): ").lower()
    else:
        sys.exit("Thanks for playing")
