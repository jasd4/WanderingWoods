import pygame as pg
from grid import Grid
from player import Player

def main():
    pg.init()
    screen = pg.display.set_mode((480, 480))
    pg.display.set_caption("Wandering Woods")

    grid_size = (6, 6)
    grid = Grid(grid_size[0], grid_size[1])

    # Create two players at opposite corners
    player1 = Player(0, 0, grid_size, color=(255, 0, 0))  # Red in top-left
    player2 = Player(5, 5, grid_size, color=(0, 0, 255))  # Blue in bottom-right

    players = [player1, player2]

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                return

        screen.fill((100, 100, 100))  # background color
        grid.draw(screen)

        for player in players:
            player.move()
            player.draw(screen)

        pg.display.update()
        pg.time.delay(400)  # Slow down movement

if __name__ == "__main__":
    main()
