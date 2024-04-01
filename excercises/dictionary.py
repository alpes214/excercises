"""
This is dictionaty creating examples.
Creating dictionary from lists

>>> create_dictionary_equal_lists([1], [2])
{1: 2}
    
>>> create_dictionary_equal_lists([], [])
{}

>>> create_dictionary_equal_lists(['a', 'b', 'c'], [1, 2, 3])
{'a': 1, 'b': 2, 'c': 3}

>>> create_dictionary_equal_lists(['a', 'b'], [1, 2, 3])
{'a': 1, 'b': 2}

>>> create_dictionary_equal_lists(['a', 'b', 'c'], [1, 2])
{'a': 1, 'b': 2}

"""
def create_dictionary_equal_lists(l1: list, l2: list) -> dict:
    """Create dictionay from two lists"""
    return dict(zip(l1, l2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    