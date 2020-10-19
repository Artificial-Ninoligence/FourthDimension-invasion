class Ship:

    #* Managing the ship
    def __init__(self, ai_game):
        #* Initializing and setting the ship's starting point
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #* Loading the ship image and its rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()

        #* Starting point = Bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):

        #* Draw the ship at tis current location
        self.screen.blit(self.image, self.rect)