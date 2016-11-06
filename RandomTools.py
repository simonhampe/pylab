import random

"""
Contains tools for randomization tasks
"""


def random_spanning_graph(n_nodes, edge_probability = 0.5) :
    """
    Creates a random spanning graph on a given number of nodes

    Arguments:
        n_nodes -- The number of nodes on which to construct the graph
    Keyword arguments:
        edge_probability -- The algorithm first constructs a random spanning tree and then adds
                            remaining edges with this probability. 0.5 by default.
    Returns a list of tuples, which are edges. Here, nodes are numbered from
    0 to n_nodes-1
    """
    # Start by constructing a random tree
    edges = [(a,b) for a in range(n_nodes) for b in range(a+1,n_nodes)]
    trees = [ [n] for n in range(n_nodes) ]
    tree_of = { n : n for n in range(n_nodes)}
    tree_edges = []
    infeasible_edges = []
    while len(edges) > 0 :
        nextedge = random.choice(edges)
        kept_tree = tree_of[ nextedge[0] ]
        discarded_tree = tree_of[ nextedge[1] ]
        for o in trees[ discarded_tree ] :
            tree_of[o] = kept_tree
            trees[ kept_tree ] += [o]
        tree_edges += [nextedge]
        edges.remove(nextedge)
        next_infeasibles = []
        for e in edges :
            if tree_of[ e[0] ] == tree_of[ e[1] ]:
                next_infeasibles += [e]
        for ni in next_infeasibles :
            edges.remove(ni)
            infeasible_edges += [ni]
    #Now add random remaining edges
    for ie in infeasible_edges :
        if random.random() <= edge_probability :
            tree_edges += [ie]
    return tree_edges

def discrete_brownian_motion(length, terminal_values, bounds) :
    """
    Creates a discrete tied brownian motion as an integer sequence.
    Arguments:
        length -- The lenght of the sequence
        terminal_values -- A tuple of (start_value, end_value). Fixes the start and end value.
        bounds -- A tuple of (min_value, max_value). Fixes lower and upper bounds
    Returns a list of ints
    """
    start_value, end_value = terminal_values
    min_value, max_value = bounds
    result = [start_value] * length
    result[-1] = end_value
    current_value = start_value
    for i in range(1, length-1) :
        valid_increments = []
        for delta in [-1,0,1] :
            delta_value = current_value + delta
            if delta_value > max_value or delta_value < min_value :
                continue
            if abs(end_value - delta_value) > length -i -1 :
                continue
            valid_increments += [delta]
        final_delta = random.choice(valid_increments)
        current_value = current_value + final_delta
        result[i] = current_value
    return result



