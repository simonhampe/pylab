import LabyrinthConstants

# Convention: Any key not contained is a wall

class Labyrinth :

    def __init__(self, width, height, start, data) :
        self.width = width
        self.height = height
        self.start = start
        self.data = data

    def value_at(self, column, row) :
        return self.data.get( (column, row), LabyrinthConstants.LAB_WALL)

    def get_start(self) :
        return self.start

    def scale(self, factor) :
        self.width = int(self.width * factor)
        self.height = int(self.height * factor)
        new_data = {}
        for i in range(0,self.width) :
            for j in range(0,self.height) :
                scaled_point = (int(i/factor), int(j/factor))
                if scaled_point in self.data.keys() :
                    new_data[(i,j)] = self.data[scaled_point]
        self.data = new_data


