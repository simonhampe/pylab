import random
import RandomTools
from Labyrinth import Labyrinth
from pygame import Rect
import GridTools

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
        self.room_tries = 7
        self.min_room_dims = (5,5)
        self.max_room_dims = (10,10)
        self.boundary_buffer = 5
        self.corridor_density = .3          # Between 0 and 1, indicates probability of additional corridors being added
        self.winding_coefficient = .7       # Probability of a corridors changing directions
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

    def _feasible_directions(self, position, from_list, forbidden_dir = None) :
        feasible = []
        for d in from_list :
            p = tuple(map(sum,zip(position, d)))
            if d != forbidden_dir and min(p[0],p[1],self.width-p[0]-1,self.height-p[1]-1) >= self.boundary_buffer :
                feasible += [d]
        return feasible

    def _build_corrdior(self, dict1, dict2) :
        start_point = random.choice(list(dict1.keys()))
        end_point = random.choice(list(dict2.keys()))
        current_point = start_point
        corr_dict = {}
        direction_list = [ (1,0), (-1,0) , (0,1), (0,-1) ]
        direction = (0,0)
        total_dist = GridTools.manhattan_distance(start_point, end_point)
        current_dist = total_dist
        dec_prob = .3
        thickness = 1
        while current_point != end_point :
            next_directions = self._feasible_directions( current_point, direction_list, tuple(map( lambda x : -x, direction)))
            if direction not in next_directions or random.random() <= self.winding_coefficient or dec_prob >= 1 :
                #Sort directions into those increasing and decreasing distance
                inc_dirs, dec_dirs = [],[]
                for d in next_directions :
                    if GridTools.manhattan_distance( tuple(map(sum,zip(current_point,d))), end_point) >= current_dist :
                        inc_dirs += [d]
                    else :
                        dec_dirs += [d]
                if len(dec_dirs) > 0 and (len(inc_dirs) == 0 or random.random() <= dec_prob) :
                    direction = random.choice(dec_dirs)
                else :
                    direction = random.choice(inc_dirs)
            dec_prob = dec_prob + (1/ total_dist * self.winding_coefficient**2)
            current_point = tuple(map(sum,zip(current_point, direction)))
            current_dist = GridTools.manhattan_distance(current_point, end_point)
            for q in GridTools.manhattan_disc(current_point, thickness) :
                corr_dict[q] = 0
        return corr_dict


    def generate_labyrinth(self) :
        roomlist = []
        # Construct random rooms: First pick random rectangles, then fill with cellular automata
        for t in range(self.room_tries) :
            rlft = random.randint(self.boundary_buffer, self.width - self.min_room_dims[0] - self.boundary_buffer - 1 )
            rtop = random.randint(self.boundary_buffer, self.height- self.min_room_dims[1] - self.boundary_buffer - 1 )
            rwdt = random.randint(self.min_room_dims[0]-1, min(self.max_room_dims[0], self.width - rlft - self.boundary_buffer)-2)
            rhgt = random.randint(self.min_room_dims[1]-1, min(self.max_room_dims[1], self.height - rtop - self.boundary_buffer-2))
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
