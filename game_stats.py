import pygame

class GameStats:
    #* Tracking statistics for 4th Dimension Invasion

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        #* Start the game in an ative state
        self.game_active = True

    def reset_stats(self):
        #* Initializing statistics that can change during the game
        self.ships_left = self.settings.ship_limit