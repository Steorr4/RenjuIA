import random
import time

import pygame
from game import Board

EMPTY = 0
BLACK_PIECE = 1
WHITE_PIECE = 2

class Renju:

    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.p1 = BLACK_PIECE
        self.p2 = WHITE_PIECE

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
                # x_loc = int(input("X? "))
                # y_loc = int(input("Y? "))

                '''
                |
                v Juste pour tester l'affichage des pieces avec la fonction board.disp_put
                '''
                x_loc = random.randint(0,14)
                y_loc = random.randint(0,14)
                valid_move = self.place(BLACK_PIECE,x_loc,y_loc)

                if valid_move:
                    self.board.disp_put(BLACK_PIECE,x_loc,y_loc)
                    if self.five_check(BLACK_PIECE):
                        return 1
                else:
                    print("Place deja occupée")

        else:
            while not valid_move :
                # x_loc = int(input("X? "))
                # y_loc = int(input("Y? "))
                '''idem ici'''
                x_loc = random.randint(0,14)
                y_loc = random.randint(0,14)
                valid_move = self.place(WHITE_PIECE,x_loc,y_loc)

                if valid_move:
                    self.board.disp_put(WHITE_PIECE,x_loc,y_loc)
                    if self.five_check(WHITE_PIECE):
                        return 1
                else:
                    print("Place deja occupée")

        self.turn += 1
        return 0

    def five_check(self, p_color:int) -> bool:
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

        #TODO + de tests sur les diagonales

        # Diags /
        for col in range(4,15) :
            for row in range(0, col+1) :
                if self.board.matrix[row][col-row] == p_color :
                    alignment += 1
                    if alignment == 5 : return True
                else :
                    alignment = 0
            alignment = 0

        # Diags \
        for col in range(10,-1,-1) :
            for row in range(0, 15-col) :
                if self.board.matrix[row][col+row] == p_color :
                    alignment += 1
                    if alignment == 5 : return True
                else :
                    alignment = 0
            alignment = 0

        return False

    #TODO Implementer la sequence des 3 premiers tours.
    def swap(self):
        tmp = self.p2
        self.p2 = self.p1
        self.p1 = tmp
        
    #TODO Implementer les limitations des noirs. (fourchette 3 x 3 / 4 x 4, Overline)

    def run(self):
        running = True

        # En CLI
        while running:
            print(f"Tour numero : {self.turn}")
            for e in self.board.matrix:
                print(e)

            '''
            Y'a un probleme ici c'est que quand ca attend l'input de l'utilisateur trop longtemps alors l'interface
            graphique va crash. Je suppose que c'est du au fait que ca bloque la boucle infini et que ca check pas les
            events pendant trop de temps. Normalement ca sera corrigé j'imagine en implementant l'event ou il faudra
            juste cliquer sur l'interface graphique qui ducoup n'interrompera normalement pas le programme en attendant
            l'input utilisateur comme ici. 
            |
            v
            '''
            p = self.turns()
            time.sleep(0.3) # Juste histoire que ca spam pas les pions a la vitesse de la lumiere.
            if p != 0 :
                print(f"Player {p} won !")
                # running = False


        # TODO Interface Graphique
        # while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
        pygame.quit()
