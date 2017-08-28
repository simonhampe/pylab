"""
Contains convenience functions for adding "vectors" and "matrices"
"""


def vector_neg(vector):
    """
    Takes a tuple and inverts the sign of each entry
    """
    return tuple(map(lambda x: -x, vector))


def matrix_neg(matrix):
    """
    Takes a list of tuples and inverts the sign of each entry
    """
    return list(map(lambda x: vector_neg(x), *matrix))


def vector_sum(*vectors):
    """
    This takes a list of tuples (of the same length) and returns a tuple
    which contains in each entry the sum of the corresponding entries in the vectors.
    """
    return tuple(map(sum, zip(*vectors)))


def matrix_sum(*matrices):
    """
    This takes a list of 'matrices', which are lists of tuples, and
    returns their sum as a list of tuples.
    """
    return list(map(lambda x: vector_sum(*x), zip(*matrices)))
