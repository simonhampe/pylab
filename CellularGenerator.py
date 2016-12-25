import random
from Labyrinth import Labyrinth
from MatrixTools import vector_sum, matrix_sum, vector_neg
from GridMatrix import GridMatrix
from LabyrinthConstants import LAB_WALL, LAB_FLOOR

"""
 This creates a labyrinth from a single cellular automaton
"""

class CellularGenerator :

    """
    Generates a labyrinth via a single cellular automaton running in several iterations
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chance_for_floor = 45
        self.death_limit = 3
        self.birth_limit = 5
        self.iterations =  10

    def _iterate(self, room, no_of_iterations = -1) :
        if no_of_iterations < 0 :
            no_of_iterations = self.iterations
        new_index = 0
        for it in range(0, no_of_iterations) :
            old_index = it % 2
            new_index = (it+1) % 2
            for node in room.rowwise_iterator() :
                old_node_data = node.data[old_index]
                nb_alive = len( [0 for nb in node.neighbours() if nb.data[old_index] == LAB_FLOOR])
                if old_node_data == LAB_FLOOR :
                    node.data[new_index] = LAB_FLOOR if nb_alive >= self.death_limit else LAB_WALL
                else :
                    node.data[new_index] = LAB_FLOOR if nb_alive >= self.birth_limit else LAB_WALL
        return new_index

    def generate_labyrinth(self) :
        room = GridMatrix(self.width, self.height, lambda r,c : [LAB_FLOOR, LAB_FLOOR] if random.randint(1,100) <= self.chance_for_floor else [LAB_WALL, LAB_WALL])
        data_index = self._iterate(room)
        rdict = {}
        for node in room.rowwise_iterator() :
            if node.data[data_index] == LAB_FLOOR :
                rdict[ (node.column, node.row) ] = LAB_FLOOR
        return Labyrinth(self.width, self.height, (0,0), (0,0), rdict)

