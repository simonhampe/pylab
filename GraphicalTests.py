import pygame, sys, Settings, Graphics
import PlayScreen
from pygame.locals import *

pygame.init()

start_position = (int(Settings.map_width/4), int(Settings.map_height/4))
end_position = (int(Settings.map_width*3/4), int(Settings.map_height*3/4))

#background = pygame.display.set_mode((320, 320))


pygame.display.set_caption('PyLap - Prototype')

PS = PlayScreen
BM = PS.BackgroundMap()

while True:
    
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen = pygame.display.set_mode((Settings.screen_width*Settings.sprite_width, Settings.screen_heigth*Settings.sprite_height))
       
#     screen.blit(background, (sprite_width, sprite_height), (0, 0, map_width * sprite_width, map_height * sprite_height ))
#       
#     for w in range(map_width):
#         for h in range(map_height):
#             if (w,h) == start_position:
#                 screen.blit(start, (w*sprite_width, h*sprite_height))
#             if (w,h) == end_position:
#                 screen.blit(end, (w*sprite_width, h*sprite_height))

    screen.fill((255, 255, 255))
    
    BM.move()
    BM.draw(screen)
    
    pygame.display.update()