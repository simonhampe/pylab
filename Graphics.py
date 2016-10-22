import pygame, Settings

pygame.init()

screen = pygame.display.set_mode(Settings.screen_size, pygame.RESIZABLE)
screen.fill((255, 255, 255))

Tilemap_scaled = pygame.Surface((1,1))
Tilemap_unscaled = pygame.Surface((1,1))

def load_image(filename, colorkey = None):
    image = pygame.image.load(filename)
    
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert()#_alpha()
     
    if colorkey is not None:
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        
    return image

#images
start = pygame.transform.scale(load_image(Settings.image_path + "start.png"), Settings.sprite_size)
end = pygame.transform.scale(load_image(Settings.image_path + "end.png"), Settings.sprite_size)
wall = pygame.transform.scale(load_image(Settings.image_path + "wall.jpg"), Settings.sprite_size)
floor = pygame.transform.scale(load_image(Settings.image_path + "floor.jpg"), Settings.sprite_size)

#background = load_image(Settings.image_path + "map2.jpg")


