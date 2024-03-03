import pygame
from pygame.sprite import Group

# Custom Modules
from settings import Settings
from ship import Ship
import game_functions as gf


def runGame():
    # Init Game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Space Invaders")

    ship = Ship(ai_settings, screen)
    # make a group that stores bullets
    bullets = Group()

    # While loop logic for Game
    # Reference game_functions.py for functions
    while True:
        gf.checkEvents(ai_settings, screen, ship, bullets)
        ship.update(ai_settings, screen)
        gf.updateBullets(bullets)
        gf.updateScreen(ai_settings, screen, ship, bullets)


runGame()
