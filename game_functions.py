import sys
from time import sleep
import pygame
from shuriken import Shuriken


def check_keydown_events(event, ninja):
    """Respond to keypresses."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ninja.moving_right = True
        elif event.key == pygame.K_LEFT:
            ninja.moving_left = True
        elif event.key == pygame.K_UP:
            ninja.moving_up = True
        elif event.key == pygame.K_DOWN:
            ninja.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()


def check_keyup_events(event, ninja):
    """Respond to key releases."""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ninja.moving_right = False
        elif event.key == pygame.K_LEFT:
            ninja.moving_left = False
        elif event.key == pygame.K_UP:
            ninja.moving_up = False
        elif event.key == pygame.K_DOWN:
            ninja.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ninja, shurikens, add_enemy):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ninja)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ninja)
        elif event.type == add_enemy:
            create_army(ai_settings, screen, shurikens)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ninja, shurikens, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ninja, shurikens, mouse_x, mouse_y):
    """Start a new game when the player clicks Start Game."""
    button_clicked = play_button.rect1.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Stop the lose sound and play the music
        pygame.mixer.music.play(-1, 0.0)

        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistic.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_level()
        sb.prep_ninjas()

        # Empty the list of shurikens.
        shurikens.empty()

        # Create a new army of shurikens and center the ninja.
        create_army(ai_settings, screen, shurikens)
        ninja.center_ninja()

    elif play_button.rect2.collidepoint(mouse_x, mouse_y):
        pygame.quit()
        sys.exit()


def update_screen(ai_settings, screen, stats, sb, ninja, shurikens, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.blit(ai_settings.bg_img.convert(), (0, 0))
    shurikens.draw(screen)
    ninja.blitme()

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_army(ai_settings, screen, shurikens):
    """Create an army of shurikens."""
    shuriken = Shuriken(ai_settings, screen)
    shurikens.add(shuriken)


def ninja_hit(ai_settings, stats, sb, screen, ninja, shurikens):
    """Respond to ninja being hit by shuriken."""
    if stats.ninjas_left > 0:
        # Decrement ninjas_left.
        stats.ninjas_left -= 1
        sb.prep_ninjas()

        # Empty the list of shurikens.
        shurikens.empty()

        # Create a new army and center the ninja.
        create_army(ai_settings, screen, shurikens)
        ninja.center_ninja()

        # Pause.
        sleep(2.05)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_shurikens(ai_settings, stats, sb, screen, ninja, shurikens):
    shurikens.update(stats, sb)
    for shuriken in shurikens:
        if shuriken.rect.right < 0:
            stats.s_amount += 1
            level_up(ai_settings, stats, sb)
            stats.score += ai_settings.shuriken_points
            sb.prep_score()
            check_high_score(stats, sb)
            shuriken.kill()

    # Check for collision
    if pygame.sprite.spritecollideany(ninja, shurikens):
        if stats.ninjas_left == 0:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(ai_settings.lose_sound, 1)
            ninja_hit(ai_settings, stats, sb, screen, ninja, shurikens)
        else:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(ai_settings.death_sound)
            ninja_hit(ai_settings, stats, sb, screen, ninja, shurikens)
            pygame.mixer.music.play()


def level_up(ai_settings, stats, sb):
    if stats.s_amount > 0 and stats.s_amount % 15 == 0:
        stats.level += 1
        sb.prep_level()
        ai_settings.increase_speed()


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
