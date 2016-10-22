import random

"""
Contains tools for randomization tasks
"""


def random_spanning_graph(n_nodes, edge_probability = 0.5) :
    """
    Creates a random spanning graph on a given number of nodes

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
