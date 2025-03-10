import pygame

S_HSIZE, S_VSIZE = 900, 900

class Board :
    def __init__(self):
        self.game_matrix = [[' '] * 15 for i in range(15)]
        for e in self.game_matrix:
            print(e)

        pygame.display.set_caption("Renju")
        self.screen = pygame.display.set_mode((S_HSIZE, S_VSIZE))
        self.bg = pygame.transform.scale(pygame.image.load("./game/assets/board.png"), (S_HSIZE, S_VSIZE))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()