import pygame

from gameData.LabyrinthConstants import *


class TileLibraryFromPath:
    """
    Takes a directory and looks for the appropriate images
    """

    def __init__(self, path, size):
        """
        Loads the images from the given path and scales them to the specified size
        """
        self.path = path
        self.size = size
        # Every library should have these members:
        self.player = self._load_and_process("start.png")
        self.end = self._load_and_process("end.png")
        self.wall = self._load_and_process("wall.jpg")
        self.floor = self._load_and_process("floor.jpg")

    def _load_and_process(self, filename):
        image = pygame.image.load(self.path + filename)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()

        return pygame.transform.scale(image, self.size)


def map_value_to_sprite(library, value):
    return {LAB_FLOOR: library.floor, LAB_WALL: library.wall, LAB_NIRVANA: library.wall, LAB_END: library.end}[value]
