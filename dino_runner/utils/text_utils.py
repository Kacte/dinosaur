import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

font_style = "freesansbold.ttf"
font_size = 22
text_color = (255,250,250)

def text_utils (message,
                  screen,
                  pos_x_center=SCREEN_WIDTH//2,
                  pos_y_center=SCREEN_HEIGHT//2
):
    font = pygame.font.Font(font_style, font_size)
    text = font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)