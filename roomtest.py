import random
from Labyrinth import Labyrinth

class RoomTester :

    def __init__(self,width,height) :
        self.width = width
        self.height = height

    def __nbrs(self, point) :
        result = []
        for t in [ (a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b) not in [(0,0)]] : #,(-1,1),(-1,-1),(1,-1),(1,1)]] :
            sp = tuple(map(sum, zip(point,t)))
            if sp[0] >= 0 and sp[0] < self.width and sp[1] >= 0 and sp[1] < self.height:
                result = result + [sp]
        return result

    def __bdypen(self, point, bdy) :
        dist = min( point[0], point[1], self.width - point[0] -1, self.height - point[1] -1)
        if dist < bdy :
            return ((dist+1)/bdy)**2
        else :
            return 1

    def generate_labyrinth(self) :
        bdy = 10
        initial_agent = ( random.choice(range(bdy,self.width-bdy)),
                         random.choice(range(bdy,self.height-bdy)),100)
        degen = 4
        nbbonus = 4
        queue = [initial_agent]
        dict = { (initial_agent[0], initial_agent[1]) : 0}
        while len(queue) > 0 :
            (ax,ay,ap), queue = queue[0], queue[1:]
            newprob = ap - degen
            deadnb = [p for p in self.__nbrs( (ax,ay)) if p not in dict.keys()]
            if random.randint(1,100) <= self.__bdypen((ax,ay), bdy) * ap + nbbonus*(8-len(deadnb)) :
                for nb in deadnb :
                    queue = queue + [ (nb[0],nb[1],newprob)]
                    dict[nb] = 0
        return Labyrinth(self.width, self.height, (0,0), (0,0), dict)

    # Cellular automaton 2
    # Much more homogeneous, still too many "tentacles"
    #def generate_labyrinth(self) :
    #    initial_agent = ( random.choice(range(0,self.width)),
    #                     random.choice(range(0,self.height)),100)
    #    degen = 3
    #    queue = [initial_agent]
    #    dict = { (initial_agent[0], initial_agent[1]) : 0}
    #    while len(queue) > 0 :
    #        (ax,ay,ap), queue = queue[0], queue[1:]
    #        newprob = max(0, ap - degen)
    #        if random.randint(1,100) <= ap :
    #            for nb in self.__nbrs( (ax,ay) ) :
    #                if nb not in dict.keys() :
    #                    queue = queue + [ (nb[0],nb[1],newprob)]
    #                dict[nb] = 0
    #    return Labyrinth(self.width, self.height, (0,0), (0,0), dict)

    # Cellular automaton 1
    # Gibt ziemlich ausgefranste Bilder
    #def generate_labyrinth(self) :
    #    initial_agent = ( random.choice(range(0,self.width)),
    #                     random.choice(range(0,self.height)),100)
    #    degen = 1
    #    queue = [initial_agent]
    #    dict = { (initial_agent[0], initial_agent[1]) : 0}
    #    while len(queue) > 0 :
    #        (ax,ay,ap), queue = queue[0], queue[1:]
    #        newprob = max(0, ap - degen)
    #        for nb in self.__nbrs( (ax,ay) ) :
    #            if nb not in dict.keys() :
    #                if random.randint(1,100) <= ap :
    #                    dict[nb] = 0
    #                    queue = queue + [ (nb[0],nb[1],newprob)]
    #    return Labyrinth(self.width, self.height, (0,0), (0,0), dict)


    # Random corridor generator
    # TODO Play with weights

    #def generate_labyrinth(self) :
    #    point_up = random.choice(range(1,self.height))
    #    point_down = random.choice(range(0,point_up))
    #    dict = {}
    #    for y in range(point_down,point_up+1) :
    #        dict[(0,y)] = 0
    #    for x in range(1,self.width) :
    #        point_up = random.choice( [point_up] +
    #                                 list(range(max(1,point_up-1),
    #                                            min(self.height,point_up+2))))
    #        point_down = random.choice( [point_down] + list(range(max(0,point_down-1),
    #                                          min(point_up, point_down+2))))
    #        if point_up < point_down :
    #            point_up, point_down = point_down, point_up

    #        if point_up == point_down :
    #            (point_up,point_down) = tuple(map(sum, zip(
    #                (point_up,point_down),random.choice([(1,0),(0,-1)]))))

    #        for y in range(point_down, point_up+1) :
    #            dict[(x,y)] = 0
    #    return Labyrinth( self.width, self.height, (0,0), (0,0), dict)

