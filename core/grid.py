import pygame
import random
from config.settings import *

def get_cell_from_mouse(pos):

    mouse_x, mouse_y = pos

    for row in range(ROWS):
        for col in range(COLS):

            rect = pygame.Rect(
                START_X + col * CELL_SIZE,
                START_Y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            if rect.collidepoint(mouse_x, mouse_y):
                return (row, col)

    return None


def apply_word(grid, selected_cells):

    for row, col in selected_cells:
        grid[row][col] = random.choice(ALPHABET)

    selected_cells.clear()

def create_grid_with_words(word_list):

    # สร้าง grid ว่าง
    grid = [["" for _ in range(COLS)] for _ in range(ROWS)]

    # เลือกคำที่วางได้ใน grid
    valid_words = [w for w in word_list if len(w) <= (COLS * ROWS)]

    word_count = random.randint(1,2)

    chosen_words = random.sample(valid_words, word_count)

    placed_words = []

    # วางคำยาวก่อน
    chosen_words.sort(key=len, reverse=True)

    for word in chosen_words:
        for letter in word:
            # Find an empty cell randomly
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                attempts += 1
                row = random.randint(0, ROWS - 1)
                col = random.randint(0, COLS - 1)
                
                if grid[row][col] == "":
                    grid[row][col] = letter
                    placed = True

        placed_words.append(word)

    # เติมตัวอักษรสุ่มในช่องที่ว่าง
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "":
                grid[r][c] = random.choice(ALPHABET)

    print("Placed words (Scattered):", placed_words)

    for row in grid:
        print(row)

    return grid
