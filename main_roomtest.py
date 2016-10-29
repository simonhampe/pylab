from Labyrinth import Labyrinth
from LabyrinthRenderer import LabyrinthRenderer
from LabyrinthGenerator import LabyrinthGenerator
from roomtest import RoomTester
from CaveLabGenerator import CaveLabGenerator
from Bezier import GridBezierCurve
import GridTools

w = 150
h = 50
#Points = { (0,0) : 1, (1,0) : 0, (2,0) : 0 }
#LG = LabyrinthGenerator(w,h)
#L = Labyrinth(w,h,(1,0), (2,0), Points);
LG = CaveLabGenerator(w,h)
L = LG.generate_labyrinth()
#G = GridBezierCurve( (10,10), (100,15), (15,20) )
#D = {}
#G.write_to_dictionary(D, 1000,1)
#L = Labyrinth(w,h,(0,0), (0,0), D)
LR = LabyrinthRenderer(L)
LR.draw()
