from Labyrinth import Labyrinth
from LabyrinthRenderer import LabyrinthRenderer
from LabyrinthGenerator import LabyrinthGenerator
from roomtest import RoomTester
from CaveLabGenerator import CaveLabGenerator
import Bezier
import GridTools
import RandomTools
import random

w = 150
h = 50
LG = CaveLabGenerator(w,h)
L = LG.generate_labyrinth()
LR = LabyrinthRenderer(L)
LR.draw()
#print(RandomTools.discrete_brownian_motion(50, (0,0), (-10,10)))
