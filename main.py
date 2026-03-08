import pygame
import sys
import random

from core.dictionary import load_words, is_valid_word
from core.grid import create_grid_with_words, get_cell_from_mouse, apply_word
from core.scoring import calculate_score

from ui.draw import draw_grid
from ui.menu import draw_menu, play_button, quit_button
from ui.buttons import draw_reroll, reroll_button

from config.settings import *

pygame.init()

# ---------------- Screen ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("60's Word Game")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 50)

# ---------------- Game States ----------------
STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
MAX_LETTER = 20

game_state = STATE_MENU

# ---------------- Load Dictionary ----------------
word_set = load_words()
valid_words = [w for w in word_set if 3 <= len(w) <= MAX_LETTER]

# ---------------- Create Grid ----------------
grid = create_grid_with_words(valid_words)

# ---------------- Game Variables ----------------
selected_cells = []
current_word = ""
score = 0
words_cleared = 0
total_words_found = 0
time_left = 60
last_tick_time = 0

# ---------------- Game Loop ----------------
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ================= MENU =================
        if game_state == STATE_MENU:

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(event.pos):
                    # Reset Game
                    score = 0
                    total_words_found = 0
                    time_left = 5
                    last_tick_time = pygame.time.get_ticks()
                    grid = create_grid_with_words(valid_words)
                    selected_cells.clear()
                    current_word = ""
                    game_state = STATE_GAME

                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # ================ GAME OVER ================
        elif game_state == STATE_GAMEOVER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_state = STATE_MENU
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # ================= GAME =================
        elif game_state == STATE_GAME:

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Right click = reset selection
                if event.button == 3:
                    selected_cells.clear()
                    current_word = ""

                # Left click
                if event.button == 1:

                    # Reroll Button
                    if reroll_button.collidepoint(event.pos):

                        grid = create_grid_with_words(valid_words)
                        words_cleared = 0
                        selected_cells.clear()
                        current_word = ""

                        print("Grid Rerolled Manually")

                    else:

                        cell = get_cell_from_mouse(event.pos)

                        if cell and cell not in selected_cells:
                            selected_cells.append(cell)
                            current_word += grid[cell[0]][cell[1]]

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and len(current_word) >= 3:

                    print("Checking:", current_word)

                    if is_valid_word(current_word, word_set):

                        gained_score = calculate_score(current_word)
                        score += gained_score
                        words_cleared += 1
                        total_words_found += 1

                        print("Valid word!")
                        print("Score gained:", gained_score)

                        print("Word Found! Rerolling grid...")
                        grid = create_grid_with_words(valid_words)
                        words_cleared = 0

                        selected_cells.clear()
                        current_word = ""

                    else:
                        print("Invalid word")

    # Timer logic (outside event loop so it ticks every frame)
    if game_state == STATE_GAME:
        current_time = pygame.time.get_ticks()
        if current_time - last_tick_time >= 1000:
            time_left -= 1
            last_tick_time = current_time

        if time_left <= 0:
            game_state = STATE_GAMEOVER

    # ================= DRAW =================
    if game_state == STATE_MENU:

        draw_menu(screen)

    elif game_state == STATE_GAME:

        screen.fill((40,40,40))

        draw_grid(screen, FONT, grid, selected_cells)

        draw_reroll(screen)

        word_text = FONT.render(current_word, True, (255,255,0))
        screen.blit(word_text, (WIDTH//2 - word_text.get_width()//2, 80))

        score_text = FONT.render(f"Score: {score}", True, (0,255,0))
        screen.blit(score_text, (50,50))

        time_text = FONT.render(f"Time: {time_left}", True, (255,100,100))
        screen.blit(time_text, (WIDTH - 250, 50))

    elif game_state == STATE_GAMEOVER:
        screen.fill((30,30,30))

        BIG_FONT = pygame.font.SysFont(None, 80)
        
        gameover_text = BIG_FONT.render("TIME'S UP!", True, (255, 100, 100))
        screen.blit(gameover_text, (WIDTH//2 - gameover_text.get_width()//2, HEIGHT//3 - 100))

        final_score_text = FONT.render(f"Final Score: {score}", True, (100, 255, 100))
        screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//3))

        words_found_text = FONT.render(f"Total Words Found: {total_words_found}", True, (255, 255, 100))
        screen.blit(words_found_text, (WIDTH//2 - words_found_text.get_width()//2, HEIGHT//3 + 60))


    pygame.display.flip()
    clock.tick(FPS)