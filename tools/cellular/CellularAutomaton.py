import random

from tools.cellular.CellularState import CellularState
from tools.cellular.GridMatrix import GridMatrix


class CellularAutomaton:
    """
    This is a cellular automaton, with two parameters death_limit and birth_limit,
    which works according to the following rules in each iteration:
    - If a cell is ALIVE and has fewer than death_limit ALIVE neighbours, it dies
    - If a cell is DEAD and has at least birth_limit ALIVE neighbours, it is reborn.

    The data is stored on a GridMatrix of fixed size. It is initially populated
    randomly, with a prescribed chance for each cell to be alive.
    The data attached to the GridMatrix is of type CellularState.
    """

    def __init__(self, grid_size, alive_ratio, death_limit, birth_limit):
        """
        Creates a new cellular generator, initializing the underlying grid
        :param grid_size: Tuple (width, height) describing the grid size.
        :param alive_ratio: Number between 0 and 100. At the beginning, each cell has this chance (in percent)
                to be alive
        :param death_limit: The death limit parameter
        :param birth_limit: The birth limit parameter
        """
        self.death_limit = death_limit
        self.birth_limit = birth_limit
        self.iterations = 0
        self.grid = GridMatrix(grid_size[0], grid_size[1],
                               lambda r, c:
                               CellularState(True) if random.randint(1, 100) < alive_ratio
                               else CellularState(False))

    def iterate(self, number_of_iterations=1):
        """
        This runs the given number of iterations on the cellular automaton.
        :param number_of_iterations: How many iterations should be run. Defaults to 1 if not given.
        """
        for i in range(0, number_of_iterations):
            for node in self.grid.rowwise_iterator():
                old_node_data = node.data.get_state(self.iterations)
                nb_alive = len([0 for nb in node.neighbours() if nb.data.get_state(self.iterations)])
                if old_node_data:
                    node.data.set_next_state(nb_alive >= self.death_limit)
                else:
                    node.data.set_next_state(nb_alive >= self.birth_limit)
            self.iterations = self.iterations + 1

    def get_connected_component(self, node):
        """
        This finds the connected component of alive cells of the given node (where connected means connected by a path
        going up, down, left and right in the grid) with respect to the last iteration.
        :param node: A node in the grid.
        :return: The connected component of the node. The component is empty, if the node itself is not alive.
        """

        if not node.data.get_last_state():
            return []
        queue = [node]
        component = []
        visited = set()
        while len(queue) > 0:
            nd, queue = queue[0], queue[1:]
            if nd not in visited:
                visited.add(nd)
                component += [nd]
                queue += [x for x in nd.straight_neighbours() if x.data.get_last_state()]
        return component

    def get_largest_component(self):
        """
        :return: A largest connected component (where connected means connected by a path
        going up, down, left and right in the grid) of alive cells in the grid with respect to the last iteration.
        The component is returned as a list of nodes.
        """
        visited = []
        max_component = []
        for node in self.grid.rowwise_iterator():
            if node in visited:
                next
            print("Computing component of ", node.row, node.column)
            node_component = self.get_connected_component(node)
            visited = visited + node_component
            if len(node_component) > len(max_component):
                max_component = node_component
        return max_component
