import pygame.font

class Scoreboard:
    #* Tracking the player's score
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #* Font settings for the score
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        #* Preparing the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        #* Rendring the score into an img
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #* Displaying the score at the center top
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midbottom = self.screen_rect.midbottom

    def prep_high_score(self):
        #* Rendering the high score into an image
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
    
        #* Displaying the high score at the center top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        #* Drawing the scoreboard on the screen
        self.screen.blit(self.score_image, self.score_rect)

        #* Drawing the high score on the screen
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        #* Checking any new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
