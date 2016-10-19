import pygame, Settings

pygame.init()

screen = pygame.display.set_mode(Settings.screen_dimensions)
screen.fill((255, 255, 255))

def load_image(filename, colorkey = None):
    image = pygame.image.load(filename)
    
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
     
    if colorkey is not None:
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        
    return image

#images
start = pygame.transform.scale(load_image(Settings.image_path + "start.png"), (Settings.sprite_width, Settings.sprite_height))
end = pygame.transform.scale(load_image(Settings.image_path + "end.png"), (Settings.sprite_width, Settings.sprite_height))
wall = pygame.transform.scale(load_image(Settings.image_path + "wall.jpg"), (Settings.sprite_width, Settings.sprite_height))
floor = pygame.transform.scale(load_image(Settings.image_path + "floor.jpg"), (Settings.sprite_width, Settings.sprite_height))

background = load_image(Settings.image_path + "map2.jpg")


