import pygame
from game import Board

class Renju:
    def __init__(self):
        self.board = Board()
        self.turn = 1

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.board.draw()
        pygame.quit()
