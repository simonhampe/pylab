
"""
Contains helper functions for general grid operations
"""

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

