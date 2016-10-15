import pygame, Settings

#images
start = pygame.transform.scale(pygame.image.load(Settings.image_path + "start.png"), (Settings.sprite_width, Settings.sprite_height))
end = pygame.transform.scale(pygame.image.load(Settings.image_path + "end.png"), (Settings.sprite_width, Settings.sprite_height))
wall = pygame.transform.scale(pygame.image.load(Settings.image_path + "wall.jpg"), (Settings.sprite_width, Settings.sprite_height))
floor = pygame.transform.scale(pygame.image.load(Settings.image_path + "floor.jpg"), (Settings.sprite_width, Settings.sprite_height))

background = pygame.image.load(Settings.image_path + "map2.jpg")


