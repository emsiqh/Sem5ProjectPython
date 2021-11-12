import pygame
from pygame.sprite import Sprite


class Ninja(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ninja, self).__init__()
        """Initialize the ninja and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ninja image and get its rect.
        self.image = pygame.image.load("Resources/Images/ninja-_2_-_1_.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ninja at the center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx

        # Store a decimal value for the ninja's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag.
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ninja's position based on the movement flag."""
        # Update the ninja's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ninja_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ninja_speed_factor
        if self.moving_up and self.rect.y > 0:
            self.centery -= self.ai_settings.ninja_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ninja_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ninja at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ninja(self):
        """Center the ninja on the screen."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
