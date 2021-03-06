import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font("Resources/fonts/Comic_Kings.ttf", 25)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ninjas()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "SCORE: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the score into a rendered image."""
        high_score = int(round(self.stats.score, -1))
        high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 10
        self.high_score_rect.top = 40

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("LEVEL: " + str(self.stats.level), True, self.text_color)

        # Center the level at the top of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.score_rect.top

    def prep_ninjas(self):
        """Show how many ninjas are left."""
        self.life_image = self.font.render("Remain: " + str(self.stats.ninjas_left), True, (255, 0, 0))

        # Center the level at the top of the screen.
        self.life_rect = self.life_image.get_rect()
        self.life_rect.left = self.screen_rect.left + 10
        self.life_rect.bottom = self.screen_rect.bottom - 10

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.life_image, self.life_rect)

