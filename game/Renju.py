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

    def loc_check(self, x:int, y:int) -> int :
        return self.board.matrix[x][y]

    def place(self, p_color: int, x:int, y:int) -> bool:
        if self.loc_check(x,y) != 0:
            return False

        self.board.matrix[x][y] = p_color
        return True

    def turns(self, x_loc, y_loc) -> int:
        if self.turn % 2 == 1 :
            if not self.place(BLACK_PIECE,x_loc,y_loc) :
                raise InvalidMove("Case impossible.")

            self.board.scene.update_case(BLACK_PIECE, x_loc, y_loc)
            # print("fork 3 check " + str(self.fork_three_check(x_loc, y_loc))) // Retourne une erreur
            if self.five_check(BLACK_PIECE):
                return 1

        else:

            if not self.place(WHITE_PIECE,x_loc,y_loc) :
                raise InvalidMove("Case impossible.")

            self.board.scene.update_case(WHITE_PIECE, x_loc, y_loc)
            if self.five_check(WHITE_PIECE):
                return 1

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

        # # Diags /
        # for col in range(4,15) :
        #     for row in range(0, col+1) :
        #         if self.board.matrix[row][col-row] == p_color :
        #             alignment += 1
        #             if alignment == 5 : return True
        #         else :
        #             alignment = 0
        #     alignment = 0
        #
        # # Diags \
        # for col in range(10,-1,-1) :
        #     for row in range(0, 15-col) :
        #         if self.board.matrix[row][col+row] == p_color :
        #             alignment += 1
        #             if alignment == 5 : return True
        #         else :
        #             alignment = 0
        #     alignment = 0

        #Diags /
        for col in range(14,-1,-1) :
            for row in range(14,-1,-1) :
                if ((self.board.matrix[row][col] == p_color) &
                        (self.board.matrix[row-1][col-1] == p_color) &
                        (self.board.matrix[row-2][col-2] == p_color) &
                        (self.board.matrix[row-3][col-3] == p_color) &
                        (self.board.matrix[row-4][col-4] == p_color)) :
                    return True

        #Diags \
        for col in range(11):
            for row in range(11):
                if ((self.board.matrix[row][col] == p_color) &
                        (self.board.matrix[row+1][col+1] == p_color) &
                        (self.board.matrix[row+2][col+2] == p_color) &
                        (self.board.matrix[row+3][col+3] == p_color) &
                        (self.board.matrix[row+4][col+4] == p_color)) :
                    return True


        return False

    #TODO Implementer la sequence des 3 premiers tours.
    def swap(self):
        tmp = self.p2
        self.p2 = self.p1
        self.p1 = tmp
        
    #TODO Implementer les limitations des noirs. (fourchette 3 x 3 / 4 x 4, Overline)
    #TODO implementer pass (si les deux joueurs sautent le tour à la suite -> draw)

    def overline_check(self, row:int) -> bool :
        count_black = 0
        first_is_black = (self.board.matrix[row][0]==BLACK_PIECE)
        for col in range(7) : #on regarde les six premiers elements de la ligne
            if self.board.matrix[row][col] == BLACK_PIECE :
                count_black +=1
        if count_black >= 5 :
            return True
        for col in range (7,15): #pour les elements suivants, on regarde seulement si l'element au debut des "six" n'est pas noir et si celui de la fin l'est aussi
            if (not first_is_black) & self.board.matrix[row][col] == BLACK_PIECE :
                count_black +=1
                first_is_black = (self.board.matrix[row][col-6]==BLACK_PIECE)
                if count_black >= 5 :
                    return True
        print("count black + " + str(count_black))
        return False

    def open_three_vertical_check(self, row: int, col: int) -> (bool,int,int,int,int):
        assert row>=2 & row<=12

        # On regarde si la ligne est proche du bord
        if (row == 2) & (self.board.matrix[row - 1][col] == BLACK_PIECE):
            return False, -1, -1, -1, -1
        if (row == 12) & (self.board.matrix[row + 1][col] == BLACK_PIECE):
            return False, -1, -1, -1, -1

        #On cherche à voir s'il y a des pieces blanches au tour
        if (self.board.matrix[row-1][col]==WHITE_PIECE) | (self.board.matrix[row+1][col]==WHITE_PIECE) :
            return False, -1, -1, -1, -1
        if (((self.board.matrix[row-2][col]==WHITE_PIECE) & (self.board.matrix[row-1][col]==BLACK_PIECE))
                | (self.board.matrix[row+2][col]==WHITE_PIECE) & (self.board.matrix[row+1][col]==BLACK_PIECE)) :
            return False, -1, -1, -1, -1

        #On regarde la ligne
        if self.board.matrix[row-1][col]==BLACK_PIECE :
            if self.board.matrix[row-2][col]==BLACK_PIECE :
                return True, row-1, col, row-2, col
            if self.board.matrix[row+1][col]==BLACK_PIECE :
                return True, row-1, col, row+1, col

        if (self.board.matrix[row+1][col]==BLACK_PIECE) & (self.board.matrix[row+2][col]==BLACK_PIECE) :
            return True, row+1, col, row+2, col

        return False, -1, -1, -1, -1

    def open_three_horizontal_check(self, row:int, col:int) -> (bool,int,int,int,int):
        assert col >= 2 & col <= 12

        # On regarde si la colonne est proche du bord
        if (col == 2) & (self.board.matrix[row][col - 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1
        if (col == 12) & (self.board.matrix[row][col + 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1

        # On cherche à voir s'il y a des pieces blanches au tour
        if (self.board.matrix[row][col-1] == WHITE_PIECE) | (self.board.matrix[row][col+1] == WHITE_PIECE):
            return False, -1, -1, -1, -1
        if (((self.board.matrix[row][col-2] == WHITE_PIECE) & (self.board.matrix[row][col-1] == BLACK_PIECE))
                | (self.board.matrix[row][col + 2] == WHITE_PIECE) & (self.board.matrix[row][col + 1] == BLACK_PIECE)):
            return False, -1, -1, -1, -1

        #On regarde la colonne
        if self.board.matrix[row][col-1] == BLACK_PIECE :
            if self.board.matrix[row][col-2] == BLACK_PIECE :
                return True, row, col-1, row, col-2
            if self.board.matrix[row][col+1] == BLACK_PIECE :
                return True, row, col-1, row, col+1

        if (self.board.matrix[row][col+1] == BLACK_PIECE) & (self.board.matrix[row][col+2] == BLACK_PIECE):
            return True, row, col+1, row, col+2

        return False, -1, -1, -1, -1

    #Diagonale 1 = \
    def open_three_diagonal1_check(self, row:int, col:int) -> (bool, int, int, int, int):
        assert col >= 2 & col <= 12 & row >= 2 & row <= 12

        # On regarde si la diagonale est proche du bord
        if (col == 2) & (self.board.matrix[row - 1][col - 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1
        if (col == 12) & (self.board.matrix[row + 1][col + 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1

        # On cherche à voir s'il y a des pieces blanches au tour
        if (self.board.matrix[row - 1][col - 1] == WHITE_PIECE) | (self.board.matrix[row + 1][col + 1] == WHITE_PIECE):
            return False, -1, -1, -1, -1
        if (((self.board.matrix[row - 2][col - 2] == WHITE_PIECE) & (self.board.matrix[row - 1][col - 1] == BLACK_PIECE))
                | (self.board.matrix[row + 2][col + 2] == WHITE_PIECE) & (self.board.matrix[row + 1][col + 1] == BLACK_PIECE)):
            return False, -1, -1, -1, -1


        #On regarde la diagonale
        if self.board.matrix[row - 1][col - 1] == BLACK_PIECE :
            if self.board.matrix[row - 2][col - 2] == BLACK_PIECE :
                return True, row-1, col-1, row-2, col-2
            if self.board.matrix[row + 1][col + 1] == BLACK_PIECE :
                return True, row-1, col-1, row+1, col+1

        if (self.board.matrix[row + 1][col + 1] == BLACK_PIECE) & (self.board.matrix[row + 2][col + 2] == BLACK_PIECE):
            return True, row+1, col+1, row+2, col+2

        return False, -1, -1, -1, -1

    #Diagonale 2 = /
    def open_three_diagonal2_check(self, row:int, col:int) -> (bool, int, int, int, int):
        assert col >= 2 & col <= 12 & row >= 2 & row <= 12

        # On regarde si la diagonale est proche du bord
        if (col == 2) & (self.board.matrix[row + 1][col - 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1
        if (col == 12) & (self.board.matrix[row - 1][col + 1] == BLACK_PIECE):
            return False, -1, -1, -1, -1

        # On cherche à voir s'il y a des pieces blanches au tour
        if (self.board.matrix[row + 1][col - 1] == WHITE_PIECE) | (self.board.matrix[row - 1][col + 1] == WHITE_PIECE):
            return False, -1, -1, -1, -1
        if (((self.board.matrix[row + 2][col - 2] == WHITE_PIECE) & (self.board.matrix[row + 1][col - 1] == BLACK_PIECE))
                | (self.board.matrix[row - 2][col + 2] == WHITE_PIECE) & (self.board.matrix[row - 1][col + 1] == BLACK_PIECE)):
            return False, -1, -1, -1, -1


        #On regarde la diagonale
        if self.board.matrix[row - 1][col + 1] == BLACK_PIECE :
            if self.board.matrix[row - 2][col + 2] == BLACK_PIECE :
                return True, row-1, col+1, row-2, col+2
            if self.board.matrix[row + 1][col - 1] == BLACK_PIECE :
                return True, row-1,col+1, row+1, col-1

        if (self.board.matrix[row + 1][col - 1] == BLACK_PIECE) & (self.board.matrix[row + 2][col - 2] == BLACK_PIECE):
            return True, row+1, col-1, row+2, col-2

        return False, -1, -1, -1, -1

    #not_to_test doit valoir 1(vertical), 2(horizontal), 3(diag1) ou 4(diag4)
    def has_open_three(self, row:int, col:int, not_to_test:int)->bool:
        assert not_to_test==1 | not_to_test==2 | not_to_test==3 | not_to_test==4
        if (row < 2) | (row > 12) | (col < 2) | (col > 12):
            return False
        if (self.open_three_vertical_check(row, col)) & (not_to_test!=1):
            return True
        if (self.open_three_horizontal_check(row, col)) & (not_to_test != 2):
            return True
        if (self.open_three_diagonal1_check(row, col)) & (not_to_test!=3):
            return True
        if (self.open_three_diagonal2_check(row, col)) & (not_to_test!=4):
            return True
        return False

    def fork_three_check(self, row:int, col:int) -> bool:
        if (row < 2) | (row > 12) | (col < 2) | (col > 12):  # nous n'avons pas un open 3 lorsqu'on est on proche des bords
            return False

        open_three = self.open_three_vertical_check(row,col)
        if  open_three[0]:
            if ((self.has_open_three(open_three[1],open_three[2],1)) |
                    (self.has_open_three(open_three[3],open_three[4],1))):
                    return True

        open_three = self.open_three_horizontal_check(row, col)
        if open_three[0]:
            if ((self.has_open_three(open_three[1], open_three[2],2)) |
                    (self.has_open_three(open_three[3], open_three[4],2))):
                return True

        open_three = self.open_three_diagonal1_check(row, col)
        if open_three[0]:
            if ((self.has_open_three(open_three[1], open_three[2],3)) |
                    (self.has_open_three(open_three[3], open_three[4],3))):
                return True

        open_three = self.open_three_diagonal2_check(row, col)
        if open_three[0]:
            if ((self.has_open_three(open_three[1], open_three[2],4)) |
                    (self.has_open_three(open_three[3], open_three[4],4))):
                return True

        return False

    def run(self):
        running = True

        # En CLI
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False

                if ev.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = ev.pos

                    for x in range(15):
                        for y in range(15):
                            if self.board.scene.grid[x][y].collidepoint(mouse_pos) :
                                try:
                                    print(f"Mouse button pressed at {mouse_pos}") #debug
                                    if self.turns(x, y) :
                                        print(f"Player won !")
                                        running = False
                                except InvalidMove as e:
                                    print(e.message)
            pygame.display.flip()
        pygame.quit()

class InvalidMove(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)