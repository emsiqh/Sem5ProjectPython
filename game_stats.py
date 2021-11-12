class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Stat the game in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ninjas_left = self.ai_settings.ninja_limit
        self.score = 0
        self.level = 1

        # A variable to store number of shurikens being killed.
        self.s_amount = 0
