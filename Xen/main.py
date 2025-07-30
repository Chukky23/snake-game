from game import Game

g = Game()

while g.running:
    #g.playing = True
    g.curr_menu.display_menu()
    g.game_loop()


import pygame
from snakerun import run_game

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Example loop (replace with your actual menu system)
while True:
    action, score = run_game(screen, clock)

    if action == "menu":
        # Show your main menu screen
        pass
    elif action == "game_over":
        # Display a game over screen with score
        print("Game Over! Score:", score)
        # Then show menu again
    elif action == "exit":
        break

pygame.quit()