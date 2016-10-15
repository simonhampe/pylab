import sys, pygame, Settings
import PlayScreen

pygame.init()

start_position = (int(Settings.map_width/4), int(Settings.map_height/4))
end_position = (int(Settings.map_width*3/4), int(Settings.map_height*3/4))

#background = pygame.display.set_mode((320, 320))


pygame.display.set_caption('PyLap - Prototype')

PS = PlayScreen
WholeScreen = PS.WholeScreen()

screen = pygame.display.set_mode(Settings.screen_dimensions)
screen.fill((255, 255, 255))

while True:
    
    PlayScreen.exit().check()
       
#     screen.blit(background, (sprite_width, sprite_height), (0, 0, map_width * sprite_width, map_height * sprite_height ))
#       
#     for w in range(map_width):
#         for h in range(map_height):
#             if (w,h) == start_position:
#                 screen.blit(start, (w*sprite_width, h*sprite_height))
#             if (w,h) == end_position:
#                 screen.blit(end, (w*sprite_width, h*sprite_height))


    
    WholeScreen.draw(screen)
    WholeScreen.move()

    pygame.display.update()
    