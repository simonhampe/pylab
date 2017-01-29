import sys, math, pygame, Settings, Graphics
from pygame.locals import *
from pygame.tests.base_test import pygame_quit
from Labyrinth import Labyrinth

#Functions without classes
#Check user interactions
def check_user_interactions(WS):

    #key press events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] and keys[pygame.K_d]:
        pygame.quit()
        sys.exit()

    #pygame events
    for event in pygame.event.get():
        #exit event
        if (event.type == QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
        #Mouse zooming
        if event.type == pygame.MOUSEBUTTONDOWN:
            #scroll UP, zoom OUT
            if event.button == 4:
                Settings.map_scaling_factor *= 2
            #scroll DOWN, zoom IN
            if event.button == 5:
                Settings.map_scaling_factor /= 2
            Settings.map_scaling_factor = max(min(Settings.map_scaling_factor, 1), 1 / 16)
            Graphics.Tilemap_scaled = pygame.transform.scale(Graphics.Tilemap_unscaled,
                                                     (int(Graphics.Tilemap_unscaled.get_width() * Settings.map_scaling_factor),
                                                      int(Graphics.Tilemap_unscaled.get_height() * Settings.map_scaling_factor)))
            WS.Tilemap.x = 0
            WS.Tilemap.y = 0

#collection of all the action on the whole screen
class WholeScreen:

    def __init__(self, game_state):
#         self.BackgroundMap = BackgroundMap()
#         self.Healthbar = Healthbar()
#         self.Manabar = Manabar()
        self.Tilemap = Tilemap(game_state)
        Graphics.Tilemap_unscaled = self.Tilemap.generate_whole_tilemap()
        Graphics.Tilemap_scaled = Graphics.Tilemap_unscaled

    def draw(self, surface):
#         self.BackgroundMap.draw(surface)
#         self.Healthbar.draw(surface)
#         self.Manabar.draw(surface)
        self.Tilemap.draw(surface)


    def move(self):
#         self.BackgroundMap.move()
        self.Tilemap.move()

#class for moving and drawing the background map
# class BackgroundMap:
#
#     def __init__(self):
#         self.image = Graphics.background
#         self.x = 0
#         self.y = 0
#         self.position = Settings.backgroundmap_position
#         self.size = Settings.backgroundmap_size
#         self.height = Settings.background_height
#         self.width = Settings.background_width
#
#     def move(self):
#         key = pygame.key.get_pressed()
#         dist = 0.5
#
#         if key[pygame.K_DOWN]:
#             self.y += dist
#             self.y = min(self.y, self.height - self.size[1])
#         if key[pygame.K_UP]:
#             self.y -= dist
#             self.y = max(self.y, 0)
#         if key[pygame.K_RIGHT]:
#             self.x += dist
#             self.x = min(self.x, self.width - self.size[0])
#         if key[pygame.K_LEFT]:
#             self.x -= dist
#             self.x = max(self.x, 0)
#
#     def draw(self, surface):
#         surface.blit(self.image, self.position, (self.x, self.y) + self.size)

#Class for tilemap
class Tilemap():

    def __init__(self, game_state):
        self.game_state = game_state
        self.tiles =game_state.labyrinth

        self.x = 0
        self.y = 0
        self.position = Settings.map_position

        self.size_displayed = Settings.map_size_displayed                       #in pixel
        self.width_displayed, self.height_displayed = self.size_displayed       #in pixel

        self.width_displayed_in_sprites = int(self.width_displayed / Settings.sprite_width)
        self.height_displayed_in_sprites = int(self.height_displayed / Settings.sprite_height)

        self.width_in_sprites = self.tiles.width
        self.height_in_sprites = self.tiles.height

        self.width = self.width_in_sprites * Settings.sprite_width              #in pixel
        self.height = self.height_in_sprites * Settings.sprite_height           #in pixel


    def generate_whole_tilemap(self):
        dummy_surface = pygame.Surface((self.width, self.height))
        for i in range(self.height_in_sprites):
            for j in range(self.width_in_sprites):
                #Check whether floor or wall
                image = Graphics.sprite_mapper[self.tiles.value_at(i,j)]
                #draw on dummy_surface
                dummy_surface.blit(image, (j * Settings.sprite_width, i * Settings.sprite_height))
        #return dummy_surface as the whole tilemap
        return dummy_surface

    def move(self):
        key = pygame.key.get_pressed()
        dist = 5 * Settings.map_scaling_factor**(0.5)

        if key[pygame.K_DOWN]:
            if self.height_in_sprites > self.height_displayed_in_sprites / Settings.map_scaling_factor:
                self.y += dist
                self.y = min(self.y, (self.height * Settings.map_scaling_factor - self.height_displayed))
        if key[pygame.K_UP]:
            self.y -= dist
            self.y = max(self.y, 0)
        if key[pygame.K_RIGHT]:
            if self.width_in_sprites > self.width_displayed_in_sprites / Settings.map_scaling_factor:
                self.x += dist
                self.x = min(self.x, self.width * Settings.map_scaling_factor - self.width_displayed)
        if key[pygame.K_LEFT]:
            self.x -= dist
            self.x = max(self.x, 0)

    def blit_clipped(self, surface, image, i,j) :
        #Ermittle Koordinaten, an die die Grafik geblittet werden soll
        #Erster Summand ist Position des ersten Tiles. Das muss immer ganz links bzw. ganz oben geblittet werden
        #Zweiter Summand ist Position des zweiten Tiles relativ zum ersten. Es fängt da an, wo das ggf. anteilge erste Tile aufhört.
        #Die x-Koordinate muss kleiner werden, wenn wir uns nach rechts bewegen.
        #Die y-Koordinate muss kleiner werden, wenn wir uns nach unten bewegen.
        #Daher wir den Rest der Division immer vom Divisor ab.
        #Dritter Summand ist Position der nachfolgenden Tiles relativ zum vorangegangenen. Verschiebung entsprechend zweiten Tiles.
        #Durch min bzw. max regeln wir anhand des Laufindexes inwieweit die Summanden relevant sind.
        #Der zweite wird ab Laufindex = 1 relevant und bleibt ab da auch unveränderlich.
        #Der dritte wird ab Laufindex = 2 relevant und wächst dann aber auch weiter.
        image_x = j*Settings.sprite_width - (int(self.x) % Settings.sprite_width)
        image_y = i*Settings.sprite_height - (int(self.y) % Settings.sprite_height)


        #Jetzt blitte bitte
        #surface.blit(image, (image_x, image_y), (image_inner_x, image_inner_y, image_inner_width, image_inner_height))
        surface.blit(image, (image_x, image_y))


    def draw_unscaled(self, surface):
        #Laufe durch Breite und Höhe der Tilemap in Sprites +1. +1 weil die Tiles in der erste und letzten Reihe oder Spalte anteilig sein können.
        #Wenn sie nicht anteilig sind, wird das letzte Tile nicht angezeigt, seine Höhe bzw. Breite ist Null.
        #Da es trotzdem gesucht wird, suchen wir die Tiles mit Try-Except mit break bei IndexError
        for i in range(self.height_displayed_in_sprites + 1):
            for j in range(self.width_displayed_in_sprites + 1):
                #Wähle die Grafik
                image = Graphics.sprite_mapper[self.tiles.value_at(int(self.y / Settings.sprite_height) + i, int(self.x / Settings.sprite_width) + j)]

                if int(self.y / Settings.sprite_height) + i == 0 and int(self.x / Settings.sprite_width) + j == 0:
                    image = Graphics.start

                if int(self.y / Settings.sprite_height) + i == self.height_in_sprites - 1 and int(self.x / Settings.sprite_width) + j == self.width_in_sprites -1:
                    image = Graphics.end
                self.blit_clipped(surface,image, i,j)


    def draw(self, surface):
        subsurf = surface.subsurface( Settings.map_position, (self.width_displayed, self.height_displayed))
        subsurf.fill((255, 255, 255))
        subsurf.blit(Graphics.Tilemap_scaled, (Settings.sprite_width, Settings.sprite_height), (self.x, self.y) + self.size_displayed)

#class for health bar
class Healthbar:

    def __init__(self):
        self.position = Settings.healthbar_position
        self.dimensions = Settings.healthbar_size

    def draw(self, surface):
        surface.fill((187, 10, 30), self.position + self.dimensions)

#class for mana bar
class Manabar:

    def __init__(self):
        self.position = Settings.manabar_position
        self.dimensions = Settings.manabar_size

    def draw(self, surface):
        surface.fill((0, 0, 255), self.position + self.dimensions)
