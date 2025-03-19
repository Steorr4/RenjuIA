import pygame

S_HSIZE, S_VSIZE = 1200, 900
COLOR_BG = (237,188,102)
COLOR_TEST = (255,255,255,0)

class Board :
    def __init__(self):
        # Matrice du plateau
        self.matrix = [[0] * 15 for _ in range(15)]

        # Relatif a l'affichage
        pygame.display.set_caption("Renju")
        pygame.display.set_icon(pygame.image.load("./game/assets/icon.png"))
        self.screen = pygame.display.set_mode((S_HSIZE, S_VSIZE))
        self.screen.fill(COLOR_BG)
        self.board = pygame.transform.scale(pygame.image.load("./game/assets/board.png"), (S_HSIZE-300, S_HSIZE-300))
        self.screen.blit(self.board, (0, 0))

        '''
        En gros ici ce que je voulais faire c'etait de remplir les cases jouable de rectangle invisible et
        normalement il y a un fonction dans pygame pour detecter les collisions de la souris avec un rectangle.
        Je pense que ca servira pour jouer une piece justement.
        |
        v
        '''
        self.grid = [[pygame.Surface((55, 55), pygame.SRCALPHA)] * 15 for _ in range(15)]
        for i in range(15):
            for j in range(15):
                pygame.draw.rect(self.grid[i][j], COLOR_TEST, (0,0,53.5,53.5))
                self.screen.blit(self.grid[i][j], (50+i*53.5,50+j*53.5))

                # self.circle_surface = pygame.Surface((S_HSIZE, S_VSIZE), pygame.SRCALPHA)
                # pygame.draw.circle(self.circle_surface, COLOR_TEST, [75+53.5*i,75+53.5*j],23)
                # self.screen.blit(self.circle_surface, (0, 0))

        # flip
        pygame.display.flip()


    '''Ca c'est pour afficher les pions posés sur le plateau'''
    def disp_put(self, color, x, y):
        if color == 1:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rblack.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
        elif color == 2:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rwhite.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
