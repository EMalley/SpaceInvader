import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """create bullet at ships position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet at (0,0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bulletWidth, ai_settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bulletColor
        self.bulletSpeed = ai_settings.bulletSpeed

    # Draw the bullet to the screen
    def update(self):
        # update decimal value of bullet moving it up
        self.y -= self.bulletSpeed
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
