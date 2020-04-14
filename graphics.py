import pygame
import sys
import canves


class My2048:
    def __init__(self, screen):
        self.width = 285
        self.height = 350
        self.bgc = (250, 248, 240)
        self.grid_width = 60
        self.grid_bgc = [184, 173, 163]
        self.screen = screen
        self.game = canves.Game2048()
        self.matrix = self.game.setCanves()
        self.score = self.game.get_score()
        self.block = []

    def drawGraph(self):
        scoreRect = pygame.Rect([10, 3, 265, 65])
        pygame.draw.rect(self.screen, [230, 230, 230], scoreRect, 2)
        pygame.draw.rect(self.screen, [184, 173, 163], [10, 75, 265, 265], 0)
        font = pygame.font.Font(None, 28)
        for i in range(4):
            self.block.append([])
            for j in range(4):
                pygame.draw.rect(self.screen, [202, 192, 181], [15 + 65 * i, 80 + 65 * j, 60, 60], 0)
                self.block[i].append(font.render(str(self.matrix[i][j]), 1, (10, 10, 10)))
        text = font.render("Score:", 1, (10, 10, 10), [250, 248, 240])
        textpos = text.get_rect()
        textpos.right = 80
        textpos.top = 10
        self.screen.blit(text, textpos)
        text = font.render(str(self.score), 1, (10, 10, 10), [250, 248, 240])
        textpos = text.get_rect()
        textpos.center = scoreRect.center
        textpos.top += 15
        self.screen.blit(text, textpos)

    def updateGraph(self):
        font = pygame.font.Font(None, 28)
        for i in range(4):
            for j in range(4):
                self.block[i][j] = font.render(str(self.matrix[i][j]), 1, (10, 10, 10))
                if self.matrix[i][j] != 0:
                    myrect = pygame.Rect([15 + 65 * j, 80 + 65 * i, 60, 60])
                    pygame.draw.rect(self.screen, (231, 179, 132), myrect, 0)
                    textpos = self.block[i][j].get_rect()
                    textpos.center = myrect.center
                    self.screen.blit(self.block[i][j], textpos)


    def gameOver(self):
        return self.game.GameOver()

    def Up(self):
        self.matrix, self.score = self.game.Up()
        self.updateGraph()

    def Down(self):
        self.matrix, self.score = self.game.Down()
        self.updateGraph()

    def Left(self):
        self.matrix, self.score = self.game.Left()
        self.updateGraph()

    def Right(self):
        self.matrix, self.score = self.game.Right()
        self.updateGraph()

