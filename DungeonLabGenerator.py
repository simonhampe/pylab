import LabyrinthConstants
import random
from pygame import Rect
from Labyrinth import Labyrinth

"""
Contains the definition of a Labyrinth generator, which generates dungeon-style labyrinths
(i.e. lots of rectangular rooms with straight labyrinthine passages)
"""

class DungeonLabGenerator :

    def __init__(self, width, height) :
        self.width = width
        self.height = height

        self.min_room_dims = (int(width/10),int(height/10))
        self.max_room_dims = (int(width/5),int(width/5))
        avg_room_size = (self.min_room_dims[0] + self.max_room_dims[0])*(self.min_room_dims[1] + self.max_room_dims[1]) * 1/4
        self.room_tries = int(width * height / (avg_room_size)) * 50
        self.boundary_buffer = 1
        self.room_boundary_buffer = 1

    def _fill_rect(self, rc) :
        r_dict = {}
        for i in range(rc.left + self.room_boundary_buffer, rc.right - self.room_boundary_buffer) :
            for j in range(rc.top + self.room_boundary_buffer, rc.bottom - self.room_boundary_buffer) :
                r_dict[(i,j)] = LabyrinthConstants.LAB_FLOOR
        return r_dict

    def _is_valid_point(self, corridor_dict, lab_dict) :
        

    def _fill_corridors(self, lab_dict) :
        valid_points = [ (a,b) for a in range(1,self.width-2) for b in range(1,self.height-2) if (a,b) not in lab_dict.keys()]
        starting_point = random.choice(valid_points)
        valid_points.remove(starting_point)
        while len(valid_points) > 0 :




    def generate_labyrinth(self) :
        roomlist = []
        for t in range(self.room_tries) :
            rlft = random.randint(self.boundary_buffer, self.width - self.min_room_dims[0] - self.boundary_buffer - 1 )
            rtop = random.randint(self.boundary_buffer, self.height- self.min_room_dims[1] - self.boundary_buffer - 1 )
            rwdt = random.randint(self.min_room_dims[0]-1, min(self.max_room_dims[0], self.width - rlft - self.boundary_buffer)-2)
            rhgt = random.randint(self.min_room_dims[1]-1, min(self.max_room_dims[1], self.height - rtop - self.boundary_buffer-2))
            nextroom = Rect(rlft, rtop, rwdt, rhgt)
            if nextroom.collidelist(roomlist) == -1 :
                roomlist += [nextroom]

        lab_dict = {}
        room_dict_list = [self._fill_rect(r) for r in roomlist]
        for d in room_dict_list :
            lab_dict.update(d)

        start_point = random.choice(list(lab_dict))
        end_point = random.choice(list(lab_dict))

        return Labyrinth(self.width, self.height, start_point, end_point, lab_dict)

