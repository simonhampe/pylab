import pygame
from pygame.rect import Rect


class TileMatrix:
    """
    This class handles the matrix of sprites which are arranged in a grid in a single image file. A single sprite can be
    extracted by its zero-based row and column numbers.
    """

    def __init__(self, image_file_name, size):
        """

        :param image_file_name: complete path of image file
        :param size: tuple (width, height), describing the size of one tile
        """
        self.image = self._load_and_process(image_file_name)
        self.size = size

    def get_tile(self, row, column):
        """
        Extracts subsurface at position row, column from given image surface
        :param row: zero-based row to extract from given image
        :param column: zero-based column to extract from given image
        :rtype pygame.Surface
        :return subsurface to be blitted
        """
        return self.image.subsurface(Rect(row * self.size[0], self.size[0], column * self.size[1], self.size[1]))

    def _load_and_process(self, filename):
        to_load = pygame.image.load(filename)
        if to_load.get_alpha() is None:
            to_load = to_load.convert()
        else:
            to_load = to_load.convert_alpha()

        return to_load
