import random
from Labyrinth import Labyrinth
import GridTools
from GridMatrix import GridMatrix
from LabyrinthConstants import *

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
        self.iterations = 3

    def _iterate(self, room, no_of_iterations = -1) :
        if no_of_iterations < 0 :
            no_of_iterations = self.iterations
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
        room.data_index = new_index

    def _component(self,room,node) :
        if node.data[room.data_index] != LAB_FLOOR :
            return []
        queue = [node]
        component = []
        while len(queue) > 0 :
            nd, queue = queue[0], queue[1:]
            if(len(nd.data) == 2) :
                nd.data += [0]
                component += [nd]
                queue += [x for x in nd.straight_neighbours() if x.data[room.data_index] == LAB_FLOOR]
        return component

    def _largest_component(self,room) :
        max_component = []
        for node in room.rowwise_iterator() :
            n_cmp = self._component(room, node)
            if len(n_cmp) > len(max_component) :
                max_component = n_cmp
        return max_component


    def generate_labyrinth(self) :
        room = GridMatrix(self.width, self.height, lambda r,c : [LAB_FLOOR, LAB_FLOOR] if random.randint(1,100) <= self.chance_for_floor else [LAB_WALL, LAB_WALL])
        room.data_index = 0
        self._iterate(room)
        comp = self._largest_component(room)
        rdict = {}
        for node in comp:
            rdict[ (node.column, node.row) ] = LAB_FLOOR
        start_point = random.choice(list(rdict))
        all_end_points = sorted( rdict, key= lambda p : GridTools.manhattan_distance(start_point,p))
        end_point = all_end_points[15] #random.choice( all_end_points[ -len(all_end_points)/3 :])
        rdict[ end_point ] = LAB_END
        return Labyrinth(self.width, self.height, start_point, rdict)

