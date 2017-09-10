import pygame
import sys
from pygame import Color, draw

from pygame.constants import QUIT
from pygame.locals import Rect
from gameData import LabyrinthConstants
from generators.CellularGenerator import CellularGenerator


class MinimapRenderer:
    def __init__(self, labyrinth, field_size):
        self.labyrinth = labyrinth
        self.field_size = field_size
        self.color_map = {LabyrinthConstants.LAB_FLOOR: Color(255, 178, 102),
                          LabyrinthConstants.LAB_WALL: Color(50, 50, 50),
                          LabyrinthConstants.LAB_END: Color(0, 255, 0),
                          LabyrinthConstants.LAB_NIRVANA: Color(255, 0, 255)}

    def draw(self, surface):
        (width, height) = self.labyrinth.get_size()
        surface.lock()
        for col in range(0, width):
            for row in range(0, height):
                value = self.labyrinth.value_at(row, col)
                color = self.color_map.get(value, Color(255, 255, 255))
                draw.rect(surface, color,
                          Rect(col * self.field_size, row * self.field_size, self.field_size, self.field_size))
        surface.unlock()


pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
screen.fill((255, 255, 255))
pygame.display.set_caption('PlayerViewRenderer - Test')

generator = CellularGenerator(100, 100, 3)
labyrinth = generator.generate_labyrinth()

renderer = MinimapRenderer(labyrinth, 3)
render_surface = screen.subsurface(Rect(20, 20, 600, 600))

renderer.draw(render_surface)
pygame.display.update()

while True:

    for event in pygame.event.get():
        # exit event
        if (event.type == QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
