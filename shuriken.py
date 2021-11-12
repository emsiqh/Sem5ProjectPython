import pygame
import random
from pygame.sprite import Sprite


class Shuriken(Sprite):
    """A class to represent a single shuriken."""

    def __init__(self, ai_settings, screen):
        super(Shuriken, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the shuriken image and set its rect attribute.
        self.image = pygame.image.load("Resources/Images/shuriken.png")

        # Start each new shuriken at random position.
        self.rect = self.image.get_rect(
            center=(
                random.randint(ai_settings.screen_width + 20, ai_settings.screen_width + 100),
                random.randint(0 + 5, ai_settings.screen_height - 5),
            )
        )
        self.speed = ai_settings.shuriken_speed_factor

    def blitme(self):
        """Draw the shuriken at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self, stats, sb):
        """Move the shuriken left."""
        self.rect.move_ip(-self.speed, 0)
        # if self.rect.right < 0:
        #     stats.s_amount += 1
        #     print(stats.s_amount)
        #     if stats.s_amount > 0 and stats.s_amount % 15 == 0:
        #         stats.level += 1
        #         self.ai_settings.increase_speed()
        #     stats.score += self.ai_settings.shuriken_points
        #     sb.prep_score()
        #     self.kill()
