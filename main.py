from Labyrinth import Labyrinth
from LabyrinthRenderer import LabyrinthRenderer
from LabyrinthGenerator import LabyrinthGenerator

w = 150
h = 50
#Points = { (0,0) : 1, (1,0) : 0, (2,0) : 0 }
LG = LabyrinthGenerator(w,h)
#L = Labyrinth(w,h,(1,0), (2,0), Points);
L = LG.generate_labyrinth()
LR = LabyrinthRenderer(L)
LR.draw()
