import sys
import pygame
from settings import Settings
from ship import Ship

class FourthDimensionInvasion:

    #* Tee overall class that manage the game assets and behaviours
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("4thDimension_Invasion")

        self.ship = Ship(self)

    def run_game(self):

        #* The main loop for the game
        while True:
            #* Watch for mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #* Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #* Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    #* Creating a game instance and running it
    ai = FourthDimensionInvasion()
    ai.run_game()