import random

from gameData.Labyrinth import Labyrinth
from gameData.LabyrinthConstants import *
from tools import GridTools
from tools.cellular.CellularAutomaton import CellularAutomaton


class CellularGenerator:
    """
    Generates a labyrinth via a single cellular automaton running in several iterations
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_labyrinth(self):
        chance_for_floor = 45
        print("Creating cellular automaton")
        automaton = CellularAutomaton((self.width, self.height), chance_for_floor, 3, 5)
        print("Iterating")
        automaton.iterate(3)
        print("Creating largest component")
        component = automaton.get_largest_component()

        room_dictionary = {}
        for node in component:
            room_dictionary[(node.column, node.row)] = LAB_FLOOR
        start_point = random.choice(list(room_dictionary))
        all_end_points = sorted(room_dictionary, key=lambda p: GridTools.manhattan_distance(start_point, p))
        end_point = all_end_points[15]  # random.choice( all_end_points[ -len(all_end_points)/3 :])
        room_dictionary[end_point] = LAB_END
        return Labyrinth(self.width, self.height, start_point, room_dictionary)
