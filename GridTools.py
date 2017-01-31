import math
from functools import reduce
from operator import mul

"""
Contains helper functions for general grid operations
"""

def binom(n,k) :
    """
    Computes binomial n choose k
    """
    if n < 0:
        return 0
    denom = reduce(mul, range(n-k+1,n+1),1)
    try :
        num = math.factorial(k)
    except ValueError :
        return 0
    return int(denom/num)

def manhattan_distance(p1,p2) :
    """
    Computes the manhattan distance of two points in a grid.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def manhattan_disc(point, radius) :
    """
    Computes all points of manhattan distance at most radius from a given point,
    returns them as a list of tuples.
    """
    result = []
    for ydelta in range(-radius, radius+1) :
        remnant = radius - abs(ydelta)
        for xdelta in range(-remnant, remnant+1) :
            result += [ tuple(map(sum,zip(point,(xdelta, ydelta)))) ]
    return result

def grid_to_pixel( gc, size ) :
    """
    Converts grid coordinates to pixel coordinates.
    More precisely, returns the upper left corner of the given grid element.
    gc The grid coordinates as tuple (gx,gy)
    size The size of one grid element as tuple (size_x, size_y)
    """
    return (gc[0] * size[0], gc[1] * size[1])

def pixel_to_grid( pc, size ) :
    """
    For given pixel coordinates, returns the coordinates of the grid element
    these coordinates lie in.
    pc The pixel coordinates as tuple (gx,gy)
    size The size of one grid element as tuple (size_x, size_y)
    """
    return ( int(pc[0] // size[0]), int(pc[1] // size[1]))

