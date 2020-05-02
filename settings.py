class Settings:
    def __init__(self):
        # Alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 = right, -1 = left

        # Screen
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
