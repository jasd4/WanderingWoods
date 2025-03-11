import pygame as pg
from grid import Grid
from player import Player
from stats import Stats  # Import Stats class

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
    stats = Stats()  # Initialize step tracker

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                return

        screen.fill((100, 100, 100))  # Background color
        grid.draw(screen)

        # Move players and update step count
        for player in players:
            player.move()
        stats.increment_steps()  # Increment step counter

        # Check if players collide
        if player1.x == player2.x and player1.y == player2.y:
            message = f"Collision! Players met after {stats.get_steps()} steps"
            display_message(screen, message)  # Show message on screen
            running = False  # Stop the game

        # Draw players
        for player in players:
            player.draw(screen)

        pg.display.update()
        pg.time.delay(100)  # Slow down movement, at 100 to speed it up a bit

        def display_message(screen, message):
            """ Collision message"""
            font = pg.font.SysFont('Arial', 24)  #  font and size
            text = font.render(message, True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

            #  semi-transparent background
            bg_rect = text_rect.inflate(20, 20)  # Expand background size
            pg.draw.rect(screen, (0, 0, 0), bg_rect)  # Black background
            screen.blit(text, text_rect)  # Draw text

            pg.display.update()  # Refresh screen
            pg.time.delay(3000)  # Show message for 3 seconds

    print(f"Game Over! Players met after {stats.get_steps()} steps.")

if __name__ == "__main__":
    main()
