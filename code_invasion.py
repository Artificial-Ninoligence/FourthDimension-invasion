import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class FourthDimensionInvasion:
    #* Tee overall class that manage the game assets and behaviours
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        #! SCREEN SIZE in SETTINGS:
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #! FULL SCREEN MODE:
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("4thDimension_Invasion")

        #! Game Instance for storing game statistics
        self.stats = GameStats(self)

        #! Ship Instance for creating the ship
        self.ship = Ship(self)

        #! Bullet Instance for creating the bullets
        self.bullets = pygame.sprite.Group()

        #! Alien Instance for creting the alien and the fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        #* The main loop for the game
        while True:
            #* Watch for mouse and keyboard events
            self._check_events()

            if self.stats.game_active:
                #* Calling the ship's update() method in the loop
                self.ship.update()

                #* Calling the bullet's update
                self._update_bullets()

                #* Calling the alien's update
                self._update_aliens()

            #* Redraw the screen during each pass through the loop
            self._update_screen()

#! KEYBOARD AND MOUSE EVENT CHECKER METHODS

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
        elif event.key == pygame.K_SPACE:
            #* Shoot out the bullets
            self._fire_bullet()
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

#! ALL ABOUT BULLET METHODS

    def _fire_bullet(self):
        #* Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #* Update bullet's positions
        self.bullets.update()

        #* Get rid of all bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._bullet_alien_collisions()


    def _bullet_alien_collisions(self):
        #* Getting rid both alien and the bulet that collide
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #* Destroy the existing bullets and respawning new alien fleet
            self.bullets.empty()
            self._create_fleet()


#! ALL ABOUT ALIEN METHODS

    def _update_aliens(self):
        #* Checking if the fleet at the edge
        self._check_fleet_edges()

        #* Updating all the alien's positions in the fleet
        self.aliens.update()

        #* Looking for collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #* Looking for any alien that hit the bottom edge
        self._check_aliens_bottom()

    def _create_fleet(self):
        #* Creating alien fleets

        #* Making alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #* Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (6 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #* Creating the the full alien fleet
        for row_number in range(number_rows):    
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #*Creating an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        #* Checking if any alien has reached the left or right edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        #* Checking if any alien has reached the bottom edge
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #* Create the same effect as if the ship got hit
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        #* Dropping the entire fleet and change its direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


#! SHIP METHOD

    def _ship_hit(self):
        #* Responding when the ship is hit
        if self.stats.ships_left > 0:
            #* Decrementing the ship left
            self.stats.ships_left -= 1

            #* Getting rid of the remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #* Creating new fleet and centering ship
            self._create_fleet()
            self.ship.center_ship()

            #* Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

#! SCREEN METHOD

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        #* Make the most recently drawn screen visible
        pygame.display.flip()

#! OUTSIDE THE CLASS

if __name__ == "__main__":
    #* Creating a game instance and running it
    ai = FourthDimensionInvasion()
    ai.run_game()