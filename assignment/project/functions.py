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


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list
    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    return [max(a, b) for a, b in zip(list1, list2)]


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
    ll = [x for x in zip(*mat)]
    return [x[i] for i, x in enumerate(ll) if i <= len(x)-1]


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary
    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''
    d3 = {**d1, **d2}
    common_keys = set(d1.keys()) & set(d2.keys())
    for k in common_keys:
        d3[k] = d1[k] + d2[k]
    return d3


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
    n = len(A)
    result = []
    # iterate over the rows of A
    for i in range(n):
        row = []
        # iterate over the columns of B
        for j in range(n):
            total = 0
            # iterate ith row of A with jth column of B dot product
            for k in range(n):
                # k implements [ith row][jth column] element-wise dot product
                total += A[i][k] * B[k][j]
            # column j of row i
            row.append(total)
        # all columns j of row i completed
        result.append(row)
    # all rows done
    return result


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
