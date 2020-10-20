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
        self.rect.midbottom = self.screen_rect.midbottom
        
        #* Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #* Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        #* Update the ship's position to the RIGHT based on the movement flag
        if self.moving_right:
            self.x += self.settings.ship_speed
        
        #* Update the ship's position to the LEFT based on the movement flag
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #* Update the ship's position to thE TOP based on the movement flag
        if self.moving_up:
            self.rect.y -= 1

        #* Update the ship's position to the BOTTOM based on the movement flag
        if self.moving_down:
            self.rect.y += 1

        self.rect.x = self.x
        


    def blitme(self):

        #* Draw the ship at tis current location
        self.screen.blit(self.image, self.rect)
