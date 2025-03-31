import pygame

from game.Text import Text

S_HSIZE, S_VSIZE = 1200, 900
COLOR_BG = (237,188,102)
COLOR_TEST = (255,255,255)

class GameScene :

    def __init__(self):

        pygame.display.set_caption("Renju")
        pygame.display.set_icon(pygame.image.load("./game/assets/icon.png"))

        self.screen = pygame.display.set_mode((S_HSIZE, S_VSIZE))
        self.board = pygame.transform.scale(pygame.image.load("./game/assets/board.png"), (S_HSIZE-300, S_HSIZE-300))
        self.screen.blit(self.board, (0, 0))

        self.menu_surf = pygame.Surface((300, S_VSIZE))
        self.menu_surf.fill(COLOR_BG)
        self.menu_turn_surf = pygame.Surface((300, 75))
        self.menu_player_surf = pygame.Surface((300, 70))
        self.menu_piece_surf = pygame.Surface((300, 70))

        self.retry = None
        self.quit = None

        self.menu_surf.blit(self.menu_turn_surf, (0, 0))
        self.menu_surf.blit(self.menu_player_surf, (0, 75))
        self.menu_surf.blit(self.menu_piece_surf, (0, 145))

        self.grid = [[_]*15 for _ in range(15)]
        self.case_surf = pygame.Surface((S_HSIZE-300, S_VSIZE))
        self.case_surf.blit(self.screen, (0, 0))
        for i in range(15):
            for j in range(15):
                self.grid[i][j] = pygame.draw.rect(self.case_surf, COLOR_TEST, (50+i*53.5,50+j*53.5,53.5,53.5))
                pygame.display.flip()

        self.update_turn(f"Tour n°1")
        self.update_player(f"Joueur 1 joue","avec les noirs.")

    def update_case(self, color, x, y):
        print(f"UPDATE: {x}, {y}") #DEBUG
        if color == 1:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rblack.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
        elif color == 2:
            piece = pygame.transform.scale(pygame.image.load("./game/assets/rwhite.png"),(53.5,53.5))
            self.screen.blit(piece, (50+x*53.5,50+y*53.5))
        pygame.display.flip()

    def update_turn(self, s: str):
        self.menu_turn_surf.fill(COLOR_BG)
        text = Text(s, (45,50))

        self.menu_turn_surf.blit(text.img, text.rect)
        self.menu_surf.blit(self.menu_turn_surf, (0,0))
        self.screen.blit(self.menu_surf, (S_HSIZE-300, 0))

    def update_player(self, s1: str, s2: str):
        self.menu_player_surf.fill(COLOR_BG)
        text1 = Text(s1, (45,50), 16,(105,105,105))
        self.menu_piece_surf.fill(COLOR_BG)
        text2 = Text(s2, (45,50), 16, (105,105,105))

        self.menu_player_surf.blit(text1.img, text1.rect)
        self.menu_piece_surf.blit(text2.img, text2.rect)

        self.menu_surf.blit(self.menu_player_surf, (0,75))
        self.menu_surf.blit(self.menu_piece_surf, (0,145))
        self.screen.blit(self.menu_surf, (S_HSIZE-300, 0))

    def disp_winning_screen(self, player: int):
        winning_screen = pygame.surface.Surface((470, 200))
        winning_screen.fill(COLOR_TEST)
        win_text = Text(f" Joueur {player} a gagné !",(0,60))
        winning_screen.blit(win_text.img, win_text.rect)

        self.retry = Text(f"Retry?", (10,175),16)
        self.quit = Text(f"Quit?", (380,175),16)
        winning_screen.blit(self.retry.img, self.retry.rect)
        winning_screen.blit(self.quit.img, self.quit.rect)


        # pygame.draw.rect(winning_screen, (0, 255, 0), self.retry.rect, 2)
        # pygame.draw.rect(winning_screen, (255, 0, 0), self.quit.rect, 2)

        self.retry = self.retry.rect
        self.quit = self.quit.rect

        self.screen.blit(winning_screen, (220,300))
        # self.screen.blit(self.board, (0, 0))

