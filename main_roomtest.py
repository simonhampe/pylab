from Labyrinth import Labyrinth
from LabyrinthRenderer import LabyrinthRenderer
from LabyrinthGenerator import LabyrinthGenerator
from roomtest import RoomTester
from CaveLabGenerator import CaveLabGenerator
import Bezier
import GridTools
import RandomTools
import MatrixTools
import random

w = 150
h = 50
LG = CaveLabGenerator(w,h)
#L = LG.generate_labyrinth()
#LR = LabyrinthRenderer(L)
#LR.draw()
l = RandomTools.smooth_discrete_brownian_motion( (0,0), [(-3,3)]*35)
print(l,len(l))
