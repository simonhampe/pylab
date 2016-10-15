import sys, pygame, Settings, Graphics
from pygame.locals import *
from pygame.tests.base_test import pygame_quit

#collection of all the action on the whole screen
class WholeScreen:
    
    def __init__(self):
        self.BackgroundMap = BackgroundMap()
        self.Healthbar = Healthbar()
        self.Manabar = Manabar()
    
    def draw(self, surface):
        self.BackgroundMap.draw(surface)
        self.Healthbar.draw(surface)
        self.Manabar.draw(surface)
    
    def move(self):
        self.BackgroundMap.move()

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