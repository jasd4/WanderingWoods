import pygame as pg

class Grid:
    def __init__(self, cols=6, rows=6, cell_size=80):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size

    def draw(self, screen):
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pg.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pg.draw.rect(screen, (0, 0, 0), rect, 1)  # Black grid lines
