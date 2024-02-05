import pygame

class Ship():
    
    def __init__(self, screen):
        """Initalize the ship and set its Starting Position"""
        self.screen = screen
        
        # Load ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.image =pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        
        # Place ship at bottom of the sreen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # make ship the right size & scale it correctly
        self.imageSize = (0,0)
        
        # Movement flags
        self.movingRight = False
        self.movingLeft = False

    def update(self):
        if self.movingRight:
            self.rect.centerx += 1
        if self.movingLeft:
            self.rect.centerx -= 1        
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)