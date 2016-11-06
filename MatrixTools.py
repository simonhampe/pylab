"""
Contains convenience functions for adding "vectors" and "matrices"
"""

def vector_sum(*vectors) :
    """
    This takes a list of tuples (of the same length) and returns a tuple
    which contains in each entry the sum of the corresponding entries in the vectors.
    """
    return tuple( map( sum, zip(*vectors)))

def matrix_sum(*matrices) :
    """
    This takes a list of 'matrices', which are lists of tuples, and
    returns their sum as a list of tuples.
    """
    return list(map( lambda x: vector_sum(*x), zip(*matrices)))

