import pygame

S_HSIZE, S_VSIZE = 1200, 900
COLOR_BG = (237,188,102)
COLOR_TEST = (255,255,255)

class GameScene :
    def __init__(self):
        pygame.display.set_caption("Renju")
        pygame.display.set_icon(pygame.image.load("./game/assets/icon.png"))

        self.screen = pygame.display.set_mode((S_HSIZE, S_VSIZE))
        self.screen.fill(COLOR_BG)
        self.board = pygame.transform.scale(pygame.image.load("./game/assets/board.png"), (S_HSIZE-300, S_HSIZE-300))
        self.screen.blit(self.board, (0, 0))

        self.grid = [[_]*15 for _ in range(15)]
        self.case_surf = pygame.Surface((S_HSIZE, S_VSIZE))
        self.case_surf.blit(self.screen, (0, 0))
        for i in range(15):
            for j in range(15):
                self.grid[i][j] = pygame.draw.rect(self.case_surf, COLOR_TEST, (50+i*53.5,50+j*53.5,53.5,53.5))
                pygame.display.flip()


    def update_case(self, color, x, y):
        print(f"UPDATE: {x}, {y}") #DEBUG
        if color == 1:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rblack.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
        elif color == 2:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rwhite.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
        pygame.display.flip()


