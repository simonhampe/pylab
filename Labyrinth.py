# Convention: Any key not contained is a wall

class Labyrinth :

    def __init__(self, width, height, start, end, data) :
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.data = data

    def scale(self, factor) :
        self.width = int(self.width * factor)
        self.height = int(self.height * factor)
        self.start = tuple( [int(x * factor) for x in self.start])
        self.end = tuple( [int(x * factor) for x in self.end])
        new_data = {}
        for i in range(0,self.width) :
            for j in range(0,self.height) :
                scaled_point = (int(i/factor), int(j/factor))
                if scaled_point in self.data.keys() :
                    new_data[(i,j)] = self.data[scaled_point]
        self.data = new_data


