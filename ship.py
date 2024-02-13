import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initalize the ship and set its Starting Position"""
        self.screen = screen
        self.aiSettings = ai_settings
        
        # Load ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.image =pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Place ship at bottom of the sreen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)
        
        # make ship the right size & scale it correctly
        self.imageSize = (0,0)
        
        # Movement flags
        self.movingRight = False
        self.movingLeft = False

    def update(self, ai_settings, screen):
        """update ships pos based on movement flags"""
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center += self.aiSettings.shipSpeed
        
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeed
                
            
        # update rect object from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)