import pygame.font


class Button:
    def __init__(self, ai_settings, screen, title, msg1, msg2):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the label.
        self.label_color = (135, 255, 91)
        self.label_rect = pygame.Rect(350, 100, 400, 350)
        self.label_font = pygame.font.Font("Resources/fonts/arfmoochikncheez.ttf", 100)

        # Set the dimensions and properties of the button.
        self.width, self.height = 250, 70
        self.button_color1 = (244, 208, 63)
        self.button_color2 = (241, 148, 138)
        self.text_color = (51, 51, 51)
        self.font = pygame.font.Font("Resources/fonts/arfmoochikncheez.ttf", 48)

        # Build the button's rect object and center it.
        self.rect1 = pygame.Rect(250, 400, self.width, self.height)
        self.rect2 = pygame.Rect(800, 400, self.width, self.height)
        # self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.prep_label(title)
        self.prep_msg1(msg1)
        self.prep_msg2(msg2)

    def prep_label(self, title):
        self.title_label = self.label_font.render(title, True, self.label_color)

    def prep_msg1(self, msg1):
        """Turn msg into a rendered image and center text on the button."""
        self.msg1_image = self.font.render(msg1, True, self.text_color,
                                           self.button_color1)
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.center = self.rect1.center

    def prep_msg2(self, msg2):
        """Turn msg into a rendered image and center text on the button."""
        self.msg2_image = self.font.render(msg2, True, self.text_color,
                                           self.button_color2)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect2.center

    def draw_button(self):
        self.screen.blit(self.title_label, self.label_rect)
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color1, self.rect1)
        self.screen.fill(self.button_color2, self.rect2)
        self.screen.blit(self.msg1_image, self.msg1_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
