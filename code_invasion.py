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
            self._check_events()
            
            #* Calling the ship's update() method in the loop
            self.ship.update()

            #* Redraw the screen during each pass through the loop
            self._update_screen()

    def _check_events(self):
        #* Respond to key and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #* Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #* Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            #* Move the ship to the left
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #* Move the ship to the left
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            #* Quit game by pressing "q"
            sys.exit()

    def _check_keyup_events(self, event):

        #* Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #* Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #* Creating a game instance and running it
    ai = FourthDimensionInvasion()
    ai.run_game()