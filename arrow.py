import pygame
from pygame.sprite import Sprite


class Arrow(Sprite):
    """A class to manage arrows fired from the ninja"""

    def __init__(self, ai_settings, screen, ninja):
        """Create an arrow object at the ninja's current position."""
        super(Arrow, self).__init__()
        self.screen = screen

        # Load the arrow image and get its rect.
        self.image = pygame.image.load("Resources/Images/arrow.png")
        self.rect = self.image.get_rect()

        # Set position.
        self.rect.centery = ninja.rect.centery
        self.rect.right = ninja.rect.right

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.speed_factor = ai_settings.arrow_speed_factor

    def update(self):
        """Move the arrow to the right."""
        # Update the decimal position of the arrow.
        self.x += self.speed_factor

        # Update the rect position.
        self.rect.x = self.x

    def blitme(self):
        """Draw the shuriken at its current location."""
        self.screen.blit(self.image, self.rect)
