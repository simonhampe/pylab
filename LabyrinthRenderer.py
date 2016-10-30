import LabyrinthConstants

class LabyrinthRenderer :

    """
    ASCII drawer for a labyrinth
    """

    def __init__(self, labyrinth) :
        self.labyrinth = labyrinth

    def draw(self) :
        for y in range(self.labyrinth.height) :
            for x in range(self.labyrinth.width) :
                try :
                    dpoint = self.labyrinth.data[(x,y)]
                    if dpoint == LabyrinthConstants.LAB_NOTHING :
                        print("X",end="")
                    if dpoint == LabyrinthConstants.LAB_FLOOR :
                        print(" ",end="")
                except KeyError:
                    print(chr(9608), end="")
            print("")
