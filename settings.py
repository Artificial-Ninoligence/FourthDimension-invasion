class Settings:
    def __init__(self):
#*Initializing the game's physical settings:
        self.screen_width = 1300
        self.screen_height = 850
        self.bg_color = (0, 0, 0)

#* Ship settings:
        self.ship_speed = 3.0
        self.ship_limit = 3

#* Bullets settings:
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (75, 75, 75)
        self.bullets_allowed = 3

#* Alien settings:
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #* 1 == right, -1 == left (Fleet Direction)
        self.fleet_direction = 1
