import pygame, sys
from pygame.locals import *

pygame.init()

image_path = "images/"

#map and sprite constants
map_width = 10
map_height = 10

sprite_width = 32
sprite_height = 32

start_position = (int(map_width/4), int(map_height/4))
end_position = (int(map_width*3/4), int(map_height*3/4))

#images
start = pygame.transform.scale(pygame.image.load(image_path + "start.png"), (sprite_width, sprite_height))
end = pygame.transform.scale(pygame.image.load(image_path + "end.png"), (sprite_width, sprite_height))
wall = pygame.transform.scale(pygame.image.load(image_path + "wall.jpg"), (sprite_width, sprite_height))
floor = pygame.transform.scale(pygame.image.load(image_path + "floor.jpg"), (sprite_width, sprite_height))
background = pygame.display.set_mode((320, 320))

pygame.display.set_caption('PyLap - Prototype')

while True:
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen = pygame.display.set_mode((map_width*sprite_width, map_height*sprite_height))
    
    for w in range(map_width):
        for h in range(map_height):
            if (w,h) == start_position:
                screen.blit(start, (w*sprite_width, h*sprite_height))
            if (w,h) == end_position:
                screen.blit(end, (w*sprite_width, h*sprite_height))

    pygame.display.update()
