import random
from Labyrinth import Labyrinth

def point_distance(p1,p2) :
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class LabyrinthGenerator :

    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def generate_labyrinth(self) :
        portrait = self.height > self.width
        comp_height = min(self.height, self.width)
        comp_width = max(self.height, self.width)

        #Pick start and end
        w_quart = int(comp_width/4)
        all_start_points = [(a,b) for a in range(w_quart) for b in range(comp_height)]
        all_end_points = [(a,b) for a in range(3*w_quart, comp_width) for b in range(comp_height)]
        start = random.choice(all_start_points)
        end = random.choice(all_end_points)

        # Transpose if necessary
        if portrait :
            start, end = map( lambda x : (x[1],x[0]), [start,end])

        dict = { start : 0, end : 1}

        return Labyrinth(self.width, self.height, start, end, dict)
