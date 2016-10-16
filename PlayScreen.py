import sys, math, pygame, Settings, Graphics
from pygame.locals import *
from pygame.tests.base_test import pygame_quit
from Labyrinth import Labyrinth

#collection of all the action on the whole screen
class WholeScreen:
    
    def __init__(self, Labyrinth):
        #self.BackgroundMap = BackgroundMap()
        self.Healthbar = Healthbar()
        self.Manabar = Manabar()
        self.Tilemap = Tilemap(Labyrinth)
    
    def draw(self, surface):
        #self.BackgroundMap.draw(surface)
        self.Healthbar.draw(surface)
        self.Manabar.draw(surface)
        self.Tilemap.draw(surface)
    
    def move(self):
#         self.BackgroundMap.move()
        self.Tilemap.move()

#class for checking user initiated exit
class exit:
    
    def check(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] and keys[pygame.K_d]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if (event.type == QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()            

#class for moving and drawing the background map
class BackgroundMap:

    def __init__(self):
        self.image = Graphics.background
        self.x = 0
        self.y = 0
        self.position = Settings.backgroundmap_position
        self.size = Settings.backgroundmap_size
        self.height = Settings.background_height
        self.width = Settings.background_width
        
    def move(self):
        key = pygame.key.get_pressed()
        dist = 0.5
        
        if key[pygame.K_DOWN]:
            self.y += dist
            self.y = min(self.y, self.height - self.size[1])
        if key[pygame.K_UP]:
            self.y -= dist
            self.y = max(self.y, 0)
        if key[pygame.K_RIGHT]:
            self.x += dist
            self.x = min(self.x, self.width - self.size[0])
        if key[pygame.K_LEFT]:
            self.x -= dist
            self.x = max(self.x, 0)
        
    def draw(self, surface):
        surface.blit(self.image, self.position, (self.x, self.y) + self.size)

#Class for tilemap
class Tilemap():
    
    def __init__(self, Labyrinth):
        self.Labyrinth = Labyrinth
        
        self.x = 0
        self.y = 0
        self.position = Settings.backgroundmap_position
        self.size = Settings.backgroundmap_size             #in pixel
        
        self.width = Labyrinth.width
        self.height = Labyrinth.height
        
        self.tiles = list()
        
        for i in range(self.height):
            self.tiles.append(list())
            for j in range(self.width):
                try:
                    dpoint = self.Labyrinth.data[(j, i)]
                    self.tiles[i].append(0)
                except KeyError:
                    self.tiles[i].append(1)

    def move(self):
        key = pygame.key.get_pressed()
        dist = 0.5
        
        if key[pygame.K_DOWN]:
            self.y += dist
            self.y = min(self.y, self.height * Settings.sprite_height - self.size[1])
        if key[pygame.K_UP]:
            self.y -= dist
            self.y = max(self.y, 0)
        if key[pygame.K_RIGHT]:
            self.x += dist
            self.x = min(self.x, self.width * Settings.sprite_width - self.size[0])
        if key[pygame.K_LEFT]:
            self.x -= dist
            self.x = max(self.x, 0)
    def draw(self, surface):
        for i in range(Settings.map_height):
            for j in range(Settings.map_width):
                #Wähle die Grafik
                if self.tiles[int(self.y / Settings.sprite_height) + i][int(self.x / Settings.sprite_width) + j] == 0:
                    image = Graphics.floor
                else:
                    image = Graphics.wall
                
                #Ermittle Koordinaten, an die die Grafik geblittet werden soll
                #Erster Summand ist Position des ersten Tiles. Das muss immer ganz rechts bzw. ganz oben geblittet werden
                #Zweiter Summand ist Position des zweiten Tiles relativ zum ersten, d.h. zur oberen oder linken Grenze der Anzeige.
                    #Die x-Koordinate muss kleiner werden, wenn wir uns nach rechts bewegen.
                    #Die y-Koordinate muss kleiner werden, wenn wir uns nach unten bewegen.
                    #Daher wir den Rest der Division immer vom Divisor ab.
                #Dritter Summand ist Position der nachfolgenden Tiles relativ zum vorangegangenen. Verschiebung entsprechend zweiten Tiles.
                #Durch min bzw. max regeln wir anhand des Laufindexes inwieweit die Summanden relevant sind.
                    #Der zweite wird ab Laufindex = 1 relevant und bleibt ab da auch unveränderlich. 
                    #Der dritte wird ab Laufindex = 2 relevant und wächst dann aber auch weiter.
                image_x = self.position[0] + min(j, 1) * (Settings.sprite_width - int(self.x) % Settings.sprite_width) + max(j - 1, 0) * Settings.sprite_width
                image_y = self.position[1] + min(i, 1) * (Settings.sprite_height - int(self.y) % Settings.sprite_height) + max(i - 1, 0) * Settings.sprite_height
           
                #Ermittle Teil der Grafik, die geblittet werden soll
                #Zuerst Startposition innerhalb der Grafik
                image_inner_x = math.ceil(int(self.x) % Settings.sprite_width) - min(1, j) * math.ceil(int(self.x) % Settings.sprite_width)
                image_inner_y = math.ceil(int(self.y) % Settings.sprite_height) - min(1, i) * math.ceil(int(self.y) % Settings.sprite_height)
                
                if j == Settings.map_width - 1:
                    image_inner_x = 0
                if i == Settings.map_height - 1:
                    image_inner_y = 0
                
                #Dann Länge und Breite innerhalb der Grafik
                image_inner_width = Settings.sprite_width - image_inner_x
                image_inner_height = Settings.sprite_height - image_inner_y
                
                if j == Settings.map_width -1:
                    image_inner_width = math.ceil(int(self.x) % Settings.sprite_width)
                if i == Settings.map_height -1:
                    image_inner_height = math.ceil(int(self.y) % Settings.sprite_height)
                                   
                #Jetzt blitte bitte
                surface.blit(image, (image_x, image_y), (image_inner_x, image_inner_y, image_inner_width, image_inner_height))

#class for health bar
class Healthbar:
    
    def __init__(self):
        self.position = Settings.healthbar_position
        self.dimensions = Settings.healthbar_dimensions
        
    def draw(self, surface):
        surface.fill((187, 10, 30), self.position + self.dimensions)

#class for mana bar
class Manabar:
    
    def __init__(self):
        self.position = Settings.manabar_position
        self.dimensions = Settings.manabar_dimensions
        
    def draw(self, surface):
        surface.fill((0, 0, 255), self.position + self.dimensions)