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
        self.bullet_width = 300
        self.bullet_height = 1500
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 300

        #alien ship(enemies)
        self.alien_ship_speed = 10.0
        self.fleet_drop_speed = 50
        self.fleet_direction  = 1
