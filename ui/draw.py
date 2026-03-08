import pygame
from config.settings import *

def draw_grid(screen, font, grid, selected_cells):

    for row in range(ROWS):
        for col in range(COLS):

            x = START_X + col * CELL_SIZE
            y = START_Y + row * CELL_SIZE

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if (row, col) in selected_cells:
                pygame.draw.rect(screen, (255, 200, 0), rect, 3)
            else:
                pygame.draw.rect(screen, (200, 200, 200), rect, 2)

            letter = grid[row][col]

            text = font.render(letter, True, (255, 255, 255))
            text_rect = text.get_rect(center=rect.center)

            screen.blit(text, text_rect)