class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (148,227,246)
        self.minion_speed_factor = 1.5
        self.minion_limit =  3
        self.speed_limit = 3

        # bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 238, 234, 64
        self.bullets_allowed = 5

        #evilminion
        self.evilminion_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1