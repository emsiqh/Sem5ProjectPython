import pygame


class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 640
        self.bg_img = pygame.image.load("Resources/Images/bg.png")

        # Sounds setting.
        self.death_sound = pygame.mixer.Sound("Resources/audios/die.mp3")
        self.lose_sound = pygame.mixer.Sound("Resources/audios/loser.mp3")

        # Ninja settings.
        self.ninja_limit = 3

        # Arrow settings.
        self.arrow_speed_factor = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Frequency of enemies appearing
        self.freq = 500

        self.ninja_speed_factor = 1.5
        self.shuriken_speed_factor = 1

        # Scoring.
        self.shuriken_points = 50

    def increase_speed(self):
        """Increase speed settings and shuriken point values."""
        # self.freq = int(self.freq / self.speedup_scale)
        self.ninja_speed_factor *= self.speedup_scale
        self.shuriken_speed_factor *= self.speedup_scale
        self.shuriken_points = int(self.shuriken_points * self.score_scale)
