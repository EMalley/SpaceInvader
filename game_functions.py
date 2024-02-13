import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        newBullet = Bullet(ai_settings, screen, ship)
        bullets.add(newBullet)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False


def checkEvents(ai_settings, screen, ship, bullets):
    """respond to key pressing and mouse events"""
    # Watch for keyboard & mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # On Key down Move Left/Right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event, ai_settings, screen, ship, bullets
            )  # Correct order
        # on Key Up stop moving
        elif event.type == pygame.KEYUP:
            check_keyup_events(
                event, ai_settings, screen, ship, bullets
            )  # Correct order


def updateScreen(ai_settings, screen, ship, bullets):
    """update images on screen and flip to new screen"""
    # Change Bg Color
    screen.fill(ai_settings.bgColor)
    # draw the ship
    ship.blitme()
    # redraw bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()
    # draw and show the screen
    pygame.display.flip()
