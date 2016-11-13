import random
import RandomTools
import Labyrinth
from Labyrinth import Labyrinth
import LabyrinthConstants
from pygame import Rect
import GridTools
from MatrixTools import vector_sum, matrix_sum, vector_neg
import Bezier

"""
Contains the definition of the cave labyrinth generator
"""

class CaveLabGenerator :

    """
    Generates a labyrinth consisting of irregular caves connected by winding corridors
    """

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.min_room_dims = (int(width/10),int(height/10))
        self.max_room_dims = (int(width/3),int(width/3))
        avg_room_size = (self.min_room_dims[0] + self.max_room_dims[0])*(self.min_room_dims[1] + self.max_room_dims[1]) * 1/4
        self.room_tries = int(width * height / (avg_room_size)) * 3
        self.boundary_buffer = int(max( self.min_room_dims[0], self.min_room_dims[1]) / 2)
        self.corridor_density = 0.1          # Between 0 and 1, indicates probability of additional corridors being added
        self.winding_number = 0
        self.room_boundary_buffer = 5

    def _point_neighbours(self, point) :
        result = []
        for t in [ (a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b) not in [(0,0)]] :
            sp = vector_sum(point,t)
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
        #room_dict = {}
        #for i in range(room.left, room.right) :
        #    for j in range(room.top, room.bottom) :
        #        room_dict[ (i,j) ] = LabyrinthConstants.LAB_FLOOR
        #return room_dict
        degen = 4
        total_room_dict = {}
        for i in range(0,3) :
            initial_agent = ( random.choice(range(room.left, room.right)), random.choice(range(room.top,room.bottom)), 100)
            queue = [initial_agent]
            #( int( (room.left + room.right)/2), int( (room.top +room.bottom)/2),100)
            room_dict = { (initial_agent[0], initial_agent[1]) : 0}
            while len(queue) > 0 :
                (ax,ay,ap), queue = queue[0], queue[1:]
                newprob = ap - degen
                deadnb = [p for p in self._point_neighbours( (ax,ay)) if p not in room_dict.keys()]
                if random.randint(1,100) <= self._boundary_penalty( room, (ax,ay), self.room_boundary_buffer) * ap :
                    for nb in deadnb :
                        queue = queue + [ (nb[0], nb[1], newprob)]
                        room_dict[nb] = LabyrinthConstants.LAB_FLOOR
            total_room_dict.update(room_dict)
        return total_room_dict

    def _feasible_directions(self, position, from_list, forbidden_dir = None) :
        feasible = []
        for d in from_list :
            p = vector_sum(position,d)
            if d != forbidden_dir and min(p[0],p[1],self.width-p[0]-1,self.height-p[1]-1) >= self.boundary_buffer :
                feasible += [d]
        return feasible

    def _shortest_straight_path_segments(self, list_of_points) :
        result = [list_of_points[0]]
        current_point = result[0]
        next_point_index = 1
        end = list_of_points[-1]
        while current_point != end :
            next_point = list_of_points[next_point_index]
            while current_point != next_point :
                dx = next_point[0] - current_point[0]
                dy = next_point[1] - current_point[1]
                if abs(dx) >= abs(dy) :
                    current_point = vector_sum(current_point,(int(dx/abs(dx)),0))
                else :
                    current_point = vector_sum(current_point, (0,int(dy/abs(dy))))
                result += [current_point]
            next_point_index = next_point_index + 1
        return result

    def _random_path_interpolation(self, list_of_points) :
        linear_pieces = self._shortest_straight_path_segments(list_of_points)
        corr_dict = {}
        xlimits = (self.boundary_buffer, self.width - self.boundary_buffer - 1)
        ylimits = (self.boundary_buffer, self.height - self.boundary_buffer -1)
        bounds = [list( map( lambda p : vector_sum(xlimits, vector_neg(p)), linear_pieces)),list( map( lambda p : vector_sum(ylimits, vector_neg(p)), linear_pieces))]
        delta = list(zip(*map(lambda x : RandomTools.discrete_brownian_motion((0,0), bounds[x],3),[0,1])))
        final_path = matrix_sum(linear_pieces, delta)
        thicknesses = RandomTools.discrete_brownian_motion( (1,1), [(1,5)]*len(final_path))
        for (i,p) in enumerate(final_path) :
            for q in GridTools.manhattan_disc(p,thicknesses[i]) :
                corr_dict[q] = LabyrinthConstants.LAB_FLOOR
        return corr_dict

    def _build_corrdior(self,dict1,dict2) :
        start_point = random.choice(list(dict1.keys()))
        end_point = random.choice(list(dict2.keys()))
        plist = [start_point]
        for i in range(0,self.winding_number) :
            plist += [ (random.randint(self.boundary_buffer,self.width - self.boundary_buffer-1), random.randint(self.boundary_buffer, self.height - self.boundary_buffer-1))]
        plist += [end_point]
        return self._random_path_interpolation(plist)


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

        start_point = random.choice(list(lab_dict))
        all_end_points = sorted( lab_dict, key= lambda p : GridTools.manhattan_distance(start_point,p))
        end_point = all_end_points[15] #random.choice( all_end_points[ -len(all_end_points)/3 :])
        print(start_point, end_point)

        return Labyrinth(self.width,self.height,start_point,end_point, lab_dict)
