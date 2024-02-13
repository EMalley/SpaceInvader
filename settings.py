class Settings:
    """A class to store all settings for Space Invaders"""

    def __init__(self):
        """initalize Game settings"""
        # Screen Setttings
        self.screen_width = 1000
        self.screen_height = 600
        self.bgColor = (230, 230, 230)

        self.shipSpeed = 1.5

        # Bullet Settings
        self.bulletSpeed = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
