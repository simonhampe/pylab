import random
from Labyrinth import Labyrinth
from pygame import Rect

class CaveLabGenerator :

    #TODO All hardcoded values should probably be relative to input
    
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.room_tries = 20
        self.min_room_dims = (10,10)
        self.max_room_dims = (20,20)
        self.boundary_buffer = 5 

    def point_neighbours(self, point) :
        result = []
        for t in [ (a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b) not in [(0,0)]] : 
            sp = tuple(map(sum, zip(point,t)))
            if sp[0] >= 0 and sp[0] < self.width and sp[1] >= 0 and sp[1] < self.height:
                result = result + [sp]
        return result
    
    def boundary_penalty(self, room, point, boundary) :
        dist = min( point[0] - room.left, point[1] - room.top, room.right - point[0], room.bottom - point[1])
        if dist < boundary :
            return ((dist+1)/boundary)**2
        else :
            return 1

    def fill_room(self, room) :
        initial_agent = ( int( (room.left + room.right)/2), int( (room.top +room.bottom)/2),100)
        degen =8 
        queue = [initial_agent]
        room_dict = { (initial_agent[0], initial_agent[1]) : 0}
        while len(queue) > 0 :
            (ax,ay,ap), queue = queue[0], queue[1:]
            newprob = ap - degen
            deadnb = [p for p in self.point_neighbours( (ax,ay)) if p not in room_dict.keys()]
            if random.randint(1,100) <= self.boundary_penalty( room, (ax,ay), 5) * ap :
                for nb in deadnb :
                    queue = queue + [ (nb[0], nb[1], newprob)]
                    room_dict[nb] = 0
        return room_dict

    def generate_labyrinth(self) :
        roomlist = []
        for t in range(self.room_tries+1) :
            rlft = random.randint(self.boundary_buffer, self.width - self.min_room_dims[0] - self.boundary_buffer)
            rtop = random.randint(self.boundary_buffer, self.height- self.min_room_dims[1] - self.boundary_buffer)
            rwdt = random.randint(self.min_room_dims[0], min(self.max_room_dims[0], self.width - rlft - self.boundary_buffer))
            rhgt = random.randint(self.min_room_dims[1], min(self.max_room_dims[1], self.height - rtop - self.boundary_buffer))
            nextroom = Rect(rlft, rtop, rwdt, rhgt)
            if nextroom.collidelist(roomlist) == -1 :
               roomlist += [nextroom]
        lab_dict = {}
        for r in roomlist :
            lab_dict.update(self.fill_room(r))
        print("Rooms: ", len(roomlist))
        return Labyrinth(self.width,self.height,(0,0),(0,0), lab_dict)
