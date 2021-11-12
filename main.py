import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ninja import Ninja
import game_functions as gf


def run_game():
    # Initialize pygame, sound, settings, and screen object.
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Resources/audios/bgm.ogg")
    pygame.mixer.music.play(-1, 0.0)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dodge Or Die - DDD")

    # Make the play button, quit button and game title.
    play_button = Button(ai_settings, screen, "DODGE OR DIE", "START GAME", "QUIT")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create a custom event for adding a new enemy
    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, ai_settings.freq)

    # Make a ninja, a group of shurikens.
    ninja = Ninja(ai_settings, screen)
    shurikens = Group()

    # Create an army of shurikens.
    gf.create_army(ai_settings, screen, shurikens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ninja, shurikens, add_enemy)
        if stats.game_active:
            ninja.update()
            gf.update_shurikens(ai_settings, stats, sb, screen, ninja, shurikens)
        gf.update_screen(ai_settings, screen, stats, sb, ninja, shurikens, play_button)


run_game()
