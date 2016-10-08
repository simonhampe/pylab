# Convention: Tile is identified by 0 (floor) / 1 (wall)

class Labyrinth :

    def __init__(self, width, height, start, end, data) :
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.data = data


