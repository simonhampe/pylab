import random
import RandomTools
from Labyrinth import Labyrinth
from pygame import Rect

"""
Contains the definition of the cave labyrinth generator
"""

class CaveLabGenerator :

    """
    Generates a labyrinth consisting of irregular caves connected by winding corridors
    """

    #TODO All hardcoded values should probably be relative to input

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.room_tries =10 
        self.min_room_dims = (10,10)
        self.max_room_dims = (20,20)
        self.boundary_buffer = 5
        self.corridor_density = .5
        self.room_boundary_buffer = 5

    def _point_neighbours(self, point) :
        result = []
        for t in [ (a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b) not in [(0,0)]] :
            sp = tuple(map(sum, zip(point,t)))
            if sp[0] >= 0 and sp[0] < self.width and sp[1] >= 0 and sp[1] < self.height:
                result = result + [sp]
        return result

    def _boundary_penalty(self, room, point, boundary) :
        dist = min( point[0] - room.left, point[1] - room.top, room.right - point[0], room.bottom - point[1])
        if dist < boundary :
            return ((dist+1)/boundary)**2
        else :
            return 1

    def _fill_room(self, room) :
        initial_agent = ( int( (room.left + room.right)/2), int( (room.top +room.bottom)/2),100)
        degen =8
        queue = [initial_agent]
        room_dict = { (initial_agent[0], initial_agent[1]) : 0}
        while len(queue) > 0 :
            (ax,ay,ap), queue = queue[0], queue[1:]
            newprob = ap - degen
            deadnb = [p for p in self._point_neighbours( (ax,ay)) if p not in room_dict.keys()]
            if random.randint(1,100) <= self._boundary_penalty( room, (ax,ay), self.room_boundary_buffer) * ap :
                for nb in deadnb :
                    queue = queue + [ (nb[0], nb[1], newprob)]
                    room_dict[nb] = 0
        return room_dict

    def _build_corrdior(self, dict1, dict2) :
        start_point = random.choice(list(dict1.keys()))
        (ex,ey) = random.choice(list(dict2.keys()))
        (cx,cy) = start_point
        corr_dict = {}
        while (cx,cy) != (ex,ey) :
            xsign = (ex > cx) - (ex < cx)
            ysign = (ey > cy) - (ey < cy)
            if abs(ex-cx) > abs(ey-cy) :
                cx += xsign
            else :
                cy += ysign
            corr_dict[(cx,cy)] = 0
        return corr_dict


    def generate_labyrinth(self) :
        roomlist = []
        # Construct random rooms: First pick random rectangles, then fill with cellular automata
        for t in range(self.room_tries+1) :
            rlft = random.randint(self.boundary_buffer, self.width - self.min_room_dims[0] - self.boundary_buffer)
            rtop = random.randint(self.boundary_buffer, self.height- self.min_room_dims[1] - self.boundary_buffer)
            rwdt = random.randint(self.min_room_dims[0], min(self.max_room_dims[0], self.width - rlft - self.boundary_buffer))
            rhgt = random.randint(self.min_room_dims[1], min(self.max_room_dims[1], self.height - rtop - self.boundary_buffer))
            nextroom = Rect(rlft, rtop, rwdt, rhgt)
            if nextroom.collidelist(roomlist) == -1 :
               roomlist += [nextroom]
        lab_dict = {}
        room_dict_list = [self._fill_room(r) for r in roomlist]
        for d in room_dict_list :
            lab_dict.update(d)

        #For corridors, pick a random spanning graph
        corridors = RandomTools.random_spanning_graph(len(roomlist), self.corridor_density)
        for c in corridors :
            lab_dict.update( self._build_corrdior( room_dict_list[c[0]], room_dict_list[c[1]]))

        return Labyrinth(self.width,self.height,(0,0),(0,0), lab_dict)
