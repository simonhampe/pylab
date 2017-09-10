import random

from gameData.Labyrinth import Labyrinth
from gameData.LabyrinthConstants import *
from tools import GridTools
from tools.cellular.CellularAutomaton import CellularAutomaton


class CellularGenerator:
    """
    Generates a labyrinth via a single cellular automaton running in several iterations
    """

    def __init__(self, width, height, margin=0):
        """
        Creates a generator
        :param width: The width of the labyrinth in tiles
        :param height: The height of the labyrinth in tiles
        :param margin: How many rows/columns of tiles at the boundary can not be floors. Defaults to 0.
        """
        self.width = width
        self.height = height
        self.margin = margin

    def generate_labyrinth(self):
        chance_for_floor = 45
        print("Creating cellular automaton for floors")
        floor_automaton = CellularAutomaton((self.width - 2 * self.margin, self.height - 2 * self.margin),
                                            chance_for_floor, 3, 5)
        print("Iterating")
        floor_automaton.iterate(3)
        print("Creating largest component")
        component = floor_automaton.get_largest_component()

        print("Creating cellular automaton for nirvana")
        nirvana_automaton = CellularAutomaton((self.width - 2 * self.margin, self.height - 2 * self.margin), 3, 1, 2)
        print("Iterating")
        nirvana_automaton.iterate(3)
        nirvana_nodes = nirvana_automaton.get_alive_nodes()

        print("Extracting data and computing start and end point")
        room_dictionary = {}
        for node in component:
            room_dictionary[(node.column + self.margin, node.row + self.margin)] = LAB_FLOOR

        start_point = random.choice(list(room_dictionary))
        all_end_points = sorted(room_dictionary, key=lambda p: GridTools.manhattan_distance(start_point, p))
        end_point = all_end_points[15]  # random.choice( all_end_points[ -len(all_end_points)/3 :])
        room_dictionary[end_point] = LAB_END

        for node in nirvana_nodes:
            shifted_coordinates = (node.column + self.margin, node.row + self.margin)
            if shifted_coordinates not in room_dictionary.keys():
                room_dictionary[shifted_coordinates] = LAB_NIRVANA

        return Labyrinth(self.width, self.height, start_point, room_dictionary)
