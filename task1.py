"""
Test 1
------
Given the 2 lists a and b, produce a distinct list c that contains only the
words that are shared by the 2 lists and let the list be sorted by number of
characters in the words. Shortest words first in the list.
"""

a = ['century', 'customer', 'democratic', 'Congress', 'customer', 'evening',
     'often', 'outside', 'reveal', 'weight', 'western', 'century']
b = ['weapon', 'western', 'traditional', 'guess', 'customer', 'exist',
     'democratic', 'Congress', 'evening', 'finish', 'western', 'executive']


def new_list(list_a: list, list_b: list) -> list:
    """
    take in two list and return distinct sorted by number of characters one
    :param list_a: list of words
    :param list_b: list of words
    :return: distinct list with words sorted by number of characters
    """
    c = [word for word in list_a if word in list_b]
    return sorted(c, key=len)


if __name__ == '__main__':
    print(new_list(a, b))