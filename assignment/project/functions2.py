def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)
    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    dic = dict()
    for x in list(string):
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return dic


def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)
    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    dic = dict()
    for k, v in d.items():
        if v in dic:
            dic[v].add(k)
        else:
            dic[v] = {k}
    return dic


def get_min(*args):
    """
    In case no argument is provided, raises ValueError exception with message.

    In case only one argument is provided, return that value.

    In case two or more arguments are provided, returns the smallest number among args.
    """
    if not len(args):
        raise ValueError
    return min(args)


def get_max(*args):
    """
    In case no argument is provided, raises ValueError exception with message.

    In case only one argument is provided, return that value.

    In case two or more arguments are provided, returns the largest number among args.
    """
    if not len(args):
        raise ValueError
    return max(args)
