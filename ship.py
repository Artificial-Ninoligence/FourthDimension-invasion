import pygame 
class Ship:

    #* Managing the ship
    def __init__(self, ai_game):

        #* Initializing and setting the ship's starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #* Loading the ship image and its rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()

        #* Starting point = Bottom center of the screen
        self.rect.center = self.screen_rect.center
        
        #* Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #* Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)

        #* Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        #* Update the ship's position to the RIGHT based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        #* Update the ship's position to the LEFT based on the movement flag
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #* Update the ship's position to thE TOP based on the movement flag
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        #* Update the ship's position to the BOTTOM based on the movement flag
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):

        #* Draw the ship at tis current location
        self.screen.blit(self.image, self.rect)
