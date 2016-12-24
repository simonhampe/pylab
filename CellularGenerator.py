import random
from Labyrinth import Labyrinth
from MatrixTools import vector_sum, matrix_sum, vector_neg
import LabyrinthConstants

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
        self.birth_limit =5 
        self.iterations =  10 


    def _fill_room(self) :
        room = []
        for i in range(0, self.height) :
            row = [LabyrinthConstants.LAB_WALL] * self.width
            for j in range(0, self.width) :
                if random.randint(1,100) <= self.chance_for_floor :
                    row[j] = LabyrinthConstants.LAB_FLOOR
            room += [row]
        return room

    def _number_of_alive_neighbours(self,room,point) :
        count = 0
        for t in [ (a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b) != (0,0)] :
            sp = vector_sum(point,t)
            if sp[0] >= 0 and sp[0] < self.height and sp[1] >= 0 and sp[1] < self.width:
                if room[sp[0]][sp[1]] == LabyrinthConstants.LAB_FLOOR :
                    count = count + 1
        return count

    def _iterate(self, room) :
        new_room = []
        for i in range(0,self.height) :
            new_room += [ [LabyrinthConstants.LAB_WALL]*self.width]
            for j in range(0,self.width) :
                nb_alive = self._number_of_alive_neighbours(room, (i,j))
                if room[i][j] == LabyrinthConstants.LAB_FLOOR :
                    new_room[i][j] = LabyrinthConstants.LAB_FLOOR if nb_alive >= self.death_limit else  LabyrinthConstants.LAB_WALL
                else :
                    new_room[i][j] = LabyrinthConstants.LAB_FLOOR if nb_alive >= self.birth_limit else  LabyrinthConstants.LAB_WALL
        return new_room

    def generate_labyrinth(self) :
        print("Filling room")
        room = self._fill_room()
        print("Iterating")
        for it in range(0, self.iterations) :
            room = self._iterate(room)
        print("Copying")
        rdict = {}
        for i in range(0,self.height) :
            for j in range(0,self.width) :
                if room[i][j] == LabyrinthConstants.LAB_FLOOR :
                    rdict[(j,i)] = LabyrinthConstants.LAB_FLOOR
        return Labyrinth(self.width, self.height, (0,0), (0,0), rdict)

