import pygame as pg
import random

class Player:
    def __init__(self, x, y, grid_size, color):   # Player position
        self.x = x
        self.y = y
        self.grid_size = grid_size
        self.color = color  # Assigned color
        self.cell_size = 80
        self.rect = pg.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)

    def move(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Random movements in all 4 directions
        dx, dy = random.choice(directions)
        new_x, new_y = self.x + dx, self.y + dy

        # Movement inside the grid
        if 0 <= new_x < self.grid_size[0] and 0 <= new_y < self.grid_size[1]:
            self.x, self.y = new_x, new_y
        self.update_position()

    def update_position(self):
        self.rect.topleft = (self.x * self.cell_size, self.y * self.cell_size)

    def draw(self, screen):  # Draw player in grid
        pg.draw.rect(screen, self.color, self.rect)

