import pygame
from config.settings import *

reroll_button = pygame.Rect(WIDTH - 200, HEIGHT - 80, 150, 50)

def draw_reroll(screen):

    BUTTON_FONT = pygame.font.SysFont(None, 45)

    mouse_pos = pygame.mouse.get_pos()

    if reroll_button.collidepoint(mouse_pos):
        color = (140,140,255)
    else:
        color = (100,100,255)

    pygame.draw.rect(screen, color, reroll_button, border_radius=10)

    text = BUTTON_FONT.render("Reroll", True, (0,0,0))
    screen.blit(text, text.get_rect(center=reroll_button.center))
