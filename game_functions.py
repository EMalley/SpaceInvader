import sys
import pygame

def checkEvents(ship):
    """respond to key pressing and mouse events"""
      # Watch for keyboard & mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    
# On Key down Move Left/Right 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True   
# on Key Up stop moving 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False
       
    
            
def updateScreen(ai_settings, screen, ship):
    """update images on screen and flip to new screen"""
    # Change Bg Color
    screen.fill(ai_settings.bgColor)
    # draw the ship
    ship.blitme()
    # draw and show the screen
    pygame.display.flip() 
    