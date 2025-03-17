import pygame

S_HSIZE, S_VSIZE = 1200, 900
COLOR_BG = (237,188,102)

class Board :
    def __init__(self):
        # Matrice du plateau
        self.matrix = [[0] * 15 for i in range(15)]

        # Relatif a l'affichage
        pygame.display.set_caption("Renju")
        self.screen = pygame.display.set_mode((S_HSIZE, S_VSIZE))
        self.screen.fill(COLOR_BG)
        #pygame.draw.rect(self.screen, COLOR_BG, pygame.Rect(S_HSIZE-300,0, S_HSIZE - S_VSIZE, S_VSIZE))
        self.board = pygame.transform.scale(pygame.image.load("./game/assets/board.png"), (S_HSIZE-300, S_HSIZE-300))

        pygame.display.flip()


    def draw(self):
        self.screen.blit(self.board, (0, 0))
        pygame.display.update()