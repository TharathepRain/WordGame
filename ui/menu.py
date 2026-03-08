import pygame
from config.settings import *

play_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 60)
quit_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 90, 200, 60)

def draw_menu(screen):

    TITLE_FONT = pygame.font.SysFont(None, 120)   # ใหญ่ขึ้น
    BUTTON_FONT = pygame.font.SysFont(None, 50)

    mouse_pos = pygame.mouse.get_pos()

    screen.fill((30,30,30))

    # -------- TITLE --------
    title = TITLE_FONT.render("60's Word Game", True, (255,255,255))
    screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//3)))

    # -------- PLAY BUTTON --------
    if play_button.collidepoint(mouse_pos):
        color = (0,255,120)   # hover glow
    else:
        color = (0,200,0)

    pygame.draw.rect(screen, color, play_button, border_radius=10)
    pygame.draw.rect(screen, (255,255,255), play_button, 2, border_radius=10)

    play_text = BUTTON_FONT.render("Play", True, (0,0,0))
    screen.blit(play_text, play_text.get_rect(center=play_button.center))

    # -------- QUIT BUTTON --------
    if quit_button.collidepoint(mouse_pos):
        color = (255,80,80)
    else:
        color = (200,0,0)

    pygame.draw.rect(screen, color, quit_button, border_radius=10)
    pygame.draw.rect(screen, (255,255,255), quit_button, 2, border_radius=10)

    quit_text = BUTTON_FONT.render("Quit", True, (0,0,0))
    screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))