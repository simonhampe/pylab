class LabyrinthRenderer :

    def __init__(self, labyrinth) :
        self.labyrinth = labyrinth

    def draw(self) :
        for y in range(self.labyrinth.height) :
            for x in range(self.labyrinth.width) :
                try :
                    dpoint = self.labyrinth.data[(x,y)]
                    print(chr(9608) if dpoint else " ", end="")
                except KeyError:
                    print("X", end="")
            print("")
