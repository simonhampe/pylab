import pygame, Settings, Graphics

class BackgroundMap:

    def __init__(self):
        self.image = Graphics.background
        self.x = 0
        self.y = 0
        
    def move(self):
        key = pygame.key.get_pressed()
        dist = 0.5
        
        if key[pygame.K_DOWN]:
            self.y += dist
            self.y = min(self.y, Graphics.background_height - Settings.backgroundmap_size[1])
        if key[pygame.K_UP]:
            self.y -= dist
            self.y = max(self.y, 0)
        if key[pygame.K_RIGHT]:
            self.x += dist
            self.x = min(self.x, Graphics.background_width - Settings.backgroundmap_size[0])
        if key[pygame.K_LEFT]:
            self.x -= dist
            self.x = max(self.x, 0)
        
    def draw(self, surface):
        surface.blit(self.image, Settings.backgroundmap_position, (self.x, self.y) + Settings.backgroundmap_size)      