import pygame

# Custom Modules
from settings import Settings
from ship import Ship
import game_functions as gf



def runGame():
    # Init Game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    
    ship = Ship(ai_settings, screen)

    # While loop logic for Game
    # Reference game_functions.py for functions
    while True:
        gf.checkEvents(ship)
        ship.update(ai_settings, screen)
        gf.updateScreen(ai_settings,screen,ship)
        
runGame()
    