import pygame
import sys
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.time import Clock

from gameData import GameState
from generators.CellularGenerator import CellularGenerator
from render import PlayerViewRenderer, GraphicSettings
from tools import GridTools

pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
screen.fill((255, 255, 255))
pygame.display.set_caption('PlayerViewRenderer - Test')

my_settings = GraphicSettings.GraphicSettings()
GS = GameState.GameState(CellularGenerator(63, 63), my_settings)

view_radius = 11
prenderer = PlayerViewRenderer.PlayerViewRenderer(GS, view_radius, my_settings)
render_surface = screen.subsurface(Rect((my_settings.sprite_width, my_settings.sprite_height), prenderer.get_size()))

prenderer.draw(render_surface)

class Updater:
    def player_moved(self, game_state):
        prenderer.draw(render_surface)
        pygame.display.update()


GS.add_update_listener(Updater())
GS.notify_player_moved()
cl = Clock()

while True:

    time_passed = cl.tick(150)

    print(1000/time_passed)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] and keys[pygame.K_d]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_s]:
        GS.move_player(GridTools.Direction.DOWN)
    if keys[pygame.K_w]:
        GS.move_player(GridTools.Direction.UP)
    if keys[pygame.K_a]:
        GS.move_player(GridTools.Direction.LEFT)
    if keys[pygame.K_d]:
        GS.move_player(GridTools.Direction.RIGHT)
    if keys[pygame.K_0]:
        GS.change_player_speed_by(0.1)
    if keys[pygame.K_9]:
        GS.change_player_speed_by(-.1)

    for event in pygame.event.get():
        # exit event
        if (event.type == QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
