"""
Using the Same Key Multiple Times

>>> create_dictionary_same_key_v1([1,2,3,1,2], [3,2,1,2,3])
{1: [3, 2], 2: [2, 3], 3: [1]}

>>> create_dictionary_same_key_v2([1,2,3,1,2], [3,2,1,2,3])
{1: [3, 2], 2: [2, 3], 3: [1]}

>>> create_dictionary_same_key_v3([1,2,3,1,2], [3,2,1,2,3])
{1: [3, 2], 2: [2, 3], 3: [1]}

"""

def create_dictionary_same_key_v1(l1: list, l2: list) -> dict:
    """ Using for loop """
    l = set(l1)
    d = {k:[] for k in l}
    
    for k,v in zip(l1,l2):
        d[k].append(v)
    
    return d


def create_dictionary_same_key_v2(l1: list, l2: list) -> dict:
    """ Using setdefault """
    d = {}
    
    for k,v in zip(l1,l2):
        group = d.setdefault(k, [])
        group.append(v)
    
    return d


from collections import defaultdict
def create_dictionary_same_key_v3(l1: list, l2: list) -> dict:
    """ Using defaultdict """
    d = defaultdict(list)
    
    for k,v in zip(l1,l2):
        d[k].append(v)
    
    # need to convert to dict
    return dict(d)


if __name__ == "__main__":
    import doctest
    doctest.testmod()