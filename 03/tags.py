from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
REPLACE_CHARS = str.maketrans('-', ' ')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    print('get_tags')
    with open('rss.xml') as f:
        tags = TAG_HTML.findall(f.read().lower())
    return [tag.translate(REPLACE_CHARS) for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    print('get_top_tags')
    print(Counter(tags).most_common(TOP_NUMBER))
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    print('get_simiarities')
    # print(tags)
    # results = {}
    # for t in tags:
    #     for t2 in tags:
    #         if t == t2:
    #             continue
    #         s = SequenceMatcher(None, t, t2)
    #         if s.ratio() > SIMILAR:
    #             results[t] = s.ratio()
    # print(results)
    for pair in product(tags, tags):
        # print(pair)
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))
        print(pair)
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            # print(pair)
            yield pair


if __name__ == "__main__":
    tags = get_tags()
    print('Tag length: {}'.format(len(tags)))
    print('Tag set: {}'.format(len(tags)))
    print('Tag set: {}'.format(set(tags)))
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
