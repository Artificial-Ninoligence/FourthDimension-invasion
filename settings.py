class Settings:
    def __init__(self):
        #*Initializing the game's static settings:
        self.screen_width = 1300
        self.screen_height = 850
        self.bg_color = (0, 0, 0)

        #* Ship settings:
        self.ship_limit = 3

        #* Bullets settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (75, 75, 75)
        self.bullets_allowed = 3

        #* Alien settings:
        self.fleet_drop_speed = 10

        #* How quickly the game speeds up
        self.speedup_scale = 1.1

        #* How quickly the alien point value increases
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        #* Settings which will change through the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.5

        #* 1 == right, -1 == left (Fleet Direction)
        self.fleet_direction = 1

        #* Score settings
        self.alien_points = 10

    def increase_speed(self):
        #* Increasing the speed and alien point's value
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)




