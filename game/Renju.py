import pygame
from game import Board

EMPTY = 0
BLACK_PIECE = 1
WHITE_PIECE = 2

class Renju:

    def __init__(self):
        self.board = Board()
        self.turn = 1

    def loc_check(self, X:int, Y:int) -> int :
        return self.board.matrix[X][Y]

    def place(self, p_color: int, X:int, Y:int) -> bool:
        if(self.loc_check(X,Y) != 0):
            return False

        self.board.matrix[X][Y] = p_color
        return True

    def turns(self) -> int:
        valid_move = False
        if self.turn % 2 == 1 :
            while not valid_move :
                x_loc = int(input("X? "))
                y_loc = int(input("Y? "))
                valid_move = self.place(BLACK_PIECE,x_loc,y_loc)
                if self.five_check(BLACK_PIECE):
                    return 1

        else:
            while not valid_move :
                x_loc = int(input("X? "))
                y_loc = int(input("Y? "))
                valid_move = self.place(WHITE_PIECE,x_loc,y_loc)
                if not valid_move :
                    print("Place deja occupée")
                if self.five_check(WHITE_PIECE):
                    return 1

        self.turn += 1
        return 0


    def five_check(self, p_color):
        alignment = 0

        # Lignes
        for row in range(15) :
            for col in range(15) :
                if self.board.matrix[row][col] == p_color :
                    alignment += 1
                    if alignment == 5 : return True
                else :
                    alignment = 0
            alignment = 0

        # Colonnes
        for col in range(15) :
            for row in range(15) :
                if self.board.matrix[row][col] == p_color :
                    alignment += 1
                    if alignment == 5 : return True
                else :
                    alignment = 0
            alignment = 0

        #TODO Manque les diags

        return False

    #TODO Implementer la sequence des 3 premiers tours.

    def run(self):
        running = True

        # En CLI
        # while running:
        #     print(f"Tour numero : {self.turn}")
        #     for e in self.board.matrix:
        #         print(e)
        #
        #     p = self.turns()
        #     if p != 0 :
        #         print(f"Joueur {p} won !")
        #         running = False

        #TODO Interface Graphique
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
            self.board.draw()
        pygame.quit()
