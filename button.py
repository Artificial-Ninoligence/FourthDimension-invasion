import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        #* Button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #* Setting for the button's dimensions and properties
        self.width, self.height = 200, 30
        self.button_color = (90, 90, 90)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #* Building the button's rect object in the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #* Prepping button's message one time only
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #* Rendering msg into image in the center of the btn
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #* Drawing a blank button and the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)