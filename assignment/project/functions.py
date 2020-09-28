def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)
    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    pass


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
    pass


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list
    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    pass


def get_diagonal(mat):
    '''
    INPUT: 2 dimensional list
    OUTPUT: list
    Given a matrix encoded as a 2 dimensional python list, return a list
    containing all the values in the diagonal starting at the index 0, 0.
    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]
    You may assume that the matrix is nonempty.
    '''
    pass


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary
    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''
    pass


def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)
    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists,  e.g.
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |

    YOU MAY NOT USE NUMPY. Write your solution in straight python.
    '''
    pass


def get_min(*args):
    """
    In case no argument is provided, raises ValueError exception with message.

    In case only one argument is provided, return that value.

    In case two or more arguments are provided, returns the smallest number among args.
    """
    pass


def get_max(*args):
    """
    In case no argument is provided, raises ValueError exception with message.

    In case only one argument is provided, return that value.

    In case two or more arguments are provided, returns the largest number among args.
    """
    pass
