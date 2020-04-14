from graphics import My2048
import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((285, 350))
    pygame.display.set_caption("2048")
    game = My2048(screen)

    while True:
        screen.fill((250, 248, 240))
        game.drawGraph()
        game.updateGraph()
        pygame.display.flip()
        if game.gameOver():
            print("Game Over")
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.Left()
                elif event.key == pygame.K_RIGHT:
                    game.Right()
                elif event.key == pygame.K_UP:
                    game.Up()
                elif event.key == pygame.K_DOWN:
                    game.Down()


if __name__ == "__main__":
    run_game()