import sys
import pygame

# Custom Modules
from settings import Settings
from ship import Ship

def runGame():
    # Init Game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    
    ship = Ship(screen)

    
    # While loop logic for Game
    while True:
        # Change Bg Color
        screen.fill(ai_settings.bgColor)
        # draw the ship
        ship.blitme()
        # Watch for keyboard & mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # draw and show the screen
        pygame.display.flip()
        
runGame()
    