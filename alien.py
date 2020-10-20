import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #* Load the alien image and set its rect attribute
        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()

        #* Selecting each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #* Storing the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        #* True == Alien at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rectx = self.x