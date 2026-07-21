class Settings:
    def __init__(self) -> None:
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.frame_rate = 60

        #ship settings
        self.ship_speed = 5.5
        self.ships_limit = 3

        #bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 30
        self.bullet_height = 150
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30

        #alien ship(enemies)
        self.alien_ship_speed = 15.0
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1

        #game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        #scorign settings
        self.alien_points = 50
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed = 5.5
        self.bullet_speed = 4.0
        self.alien_ship_speed = 15.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_ship_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
