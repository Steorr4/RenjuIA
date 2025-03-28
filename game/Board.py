import pygame
from game.GameScene import GameScene

class Board :
    def __init__(self):
        # Matrice du plateau
        self.matrix = [[0] * 15 for _ in range(15)]

        # Relatif a l'affichage
        self.scene = GameScene()
        pygame.display.flip()


