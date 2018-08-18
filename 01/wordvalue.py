from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt', 'r') as x:
        data = x.read().split()
    return data

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # Creates a list of numbers based the word arg and values per letter
    # Sums then returns total word value
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # Loads all the words from 'dictionary.txt
    if words is None:
        words = load_words()
    # Words is a list and the list is iterated over, passing each element to the
    #  key which is 'max_word_value', the item with the max value is returned.
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
