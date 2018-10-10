class Settings():

    def __init__(self):
        self.screen_width = 1050
        self.screen_height = 650
        self.bg_color = (148,227,246)
        self.minion_speed_factor = 2
        self.minion_limit =  3
        self.speed_limit = 3

        # bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 238, 234, 64
        self.bullets_allowed = 5

        #evilminion
        self.evilminion_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        #scoring
        self.evilminion_points = 50

    def initialize_dynamic_settings(self):
        self.minion_speed_factor = 3
        self.bullet_speed_factor = 3
        self.evilminion_speed_factor = 2
        self.fleet_direction = 1
        self.evilminion_points = 50

    def increase_speed(self):
        self.minion_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.evilminion_speed_factor *= self.speedup_scale
        self.evilminion_points = int(self.evilminion_points * self.score_scale)
        print(self.evilminion_points)

