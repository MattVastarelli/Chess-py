from Models import chessPiece


class Game:
    def __init__(self):
        self.white_turn = True
        self.black_turn = False
        self.x_axis = 0
        self.y_axis = 0
        self.game_board = [[0 for x in range(8)] for y in range(8)]
        self.display_board = [[0 for x in range(8)] for y in range(8)]

        # white back row
        self.whi_rook_1 = chessPiece.Rook('White', '1')
        self.whi_knight_1 = chessPiece.Knight('White', '1')
        self.whi_bishop_1 = chessPiece.Bishop('White', '1')
        self.whi_queen_1 = chessPiece.Queen('White', '1')
        self.whi_king_1 = chessPiece.King('White', '1')
        self.whi_rook_2 = chessPiece.Rook('White', '2')
        self.whi_knight_2 = chessPiece.Knight('White', '2')
        self.whi_bishop_2 = chessPiece.Bishop('White', '2')

        # white pawns
        self.whi_pawn_1 = chessPiece.Pawn('White', '1')
        self.whi_pawn_2 = chessPiece.Pawn('White', '2')
        self.whi_pawn_3 = chessPiece.Pawn('White', '3')
        self.whi_pawn_4 = chessPiece.Pawn('White', '4')
        self.whi_pawn_5 = chessPiece.Pawn('White', '5')
        self.whi_pawn_6 = chessPiece.Pawn('White', '6')
        self.whi_pawn_7 = chessPiece.Pawn('White', '7')
        self.whi_pawn_8 = chessPiece.Pawn('White', '8')

        # black back row
        self.blk_rook_1 = chessPiece.Rook('Black', '1')
        self.blk_knight_1 = chessPiece.Knight('Black', '1')
        self.blk_bishop_1 = chessPiece.Bishop('Black', '1')
        self.blk_queen_1 = chessPiece.Queen('Black', '1')
        self.blk_king_1 = chessPiece.King('Black', '1')
        self.blk_rook_2 = chessPiece.Rook('Black', '2')
        self.blk_knight_2 = chessPiece.Knight('Black', '2')
        self.blk_bishop_2 = chessPiece.Bishop('Black', '2')

        # white pawns
        self.blk_pawn_1 = chessPiece.Pawn('Black', '1')
        self.blk_pawn_2 = chessPiece.Pawn('Black', '2')
        self.blk_pawn_3 = chessPiece.Pawn('Black', '3')
        self.blk_pawn_4 = chessPiece.Pawn('Black', '4')
        self.blk_pawn_5 = chessPiece.Pawn('Black', '5')
        self.blk_pawn_6 = chessPiece.Pawn('Black', '6')
        self.blk_pawn_7 = chessPiece.Pawn('Black', '7')
        self.blk_pawn_8 = chessPiece.Pawn('Black', '8')

    # checks to see if a game is oven and who won
    def is_game_done(self, King):
        if chessPiece.King.is_alive is False:
            return chessPiece.King.get_color() + ' won'

    # checks to see  if a given move sent as a tuple is valid
    def is_move_valid(self, move):
        if move in chessPiece.King.get_valid_moves():
            return True
        elif move in chessPiece.Queen.get_valid_moves():
            return True
        elif move in chessPiece.Knight.get_valid_moves():
            return True
        elif move in chessPiece.Rook.get_valid_moves():
            return True
        elif move in chessPiece.Bishop.get_valid_moves():
            return True
        elif move in chessPiece.Pawn.get_valid_moves():
            return True
        else:
            return False

    # build the starting board
    def fill_board(self):

        # white back row
        self.game_board[7][0] = self.whi_rook_1
        self.game_board[7][1] = self.whi_knight_1
        self.game_board[7][2] = self.whi_bishop_1
        self.game_board[7][3] = self.whi_queen_1
        self.game_board[7][4] = self.whi_king_1
        self.game_board[7][5] = self.whi_bishop_2
        self.game_board[7][6] = self.whi_knight_2
        self.game_board[7][7] = self.whi_rook_2

        # white pawns
        self.game_board[6][0] = self.whi_pawn_1
        self.game_board[6][1] = self.whi_pawn_2
        self.game_board[6][2] = self.whi_pawn_3
        self.game_board[6][3] = self.whi_pawn_4
        self.game_board[6][4] = self.whi_pawn_5
        self.game_board[6][5] = self.whi_pawn_6
        self.game_board[6][6] = self.whi_pawn_7
        self.game_board[6][7] = self.whi_pawn_8

        # black back row
        self.game_board[0][0] = self.blk_rook_1
        self.game_board[0][1] = self.blk_knight_1
        self.game_board[0][2] = self.blk_bishop_1
        self.game_board[0][3] = self.blk_queen_1
        self.game_board[0][4] = self.blk_king_1
        self.game_board[0][5] = self.blk_bishop_2
        self.game_board[0][6] = self.blk_knight_2
        self.game_board[0][7] = self.blk_rook_2

        # black pawns
        self.game_board[1][0] = self.blk_pawn_1
        self.game_board[1][1] = self.blk_pawn_2
        self.game_board[1][2] = self.blk_pawn_3
        self.game_board[1][3] = self.blk_pawn_4
        self.game_board[1][4] = self.blk_pawn_5
        self.game_board[1][5] = self.blk_pawn_6
        self.game_board[1][6] = self.blk_pawn_7
        self.game_board[1][7] = self.blk_pawn_8

    # make the display matrix
    def make_display_board(self):
        # white back row
        self.display_board[7][0] = self.whi_rook_1.get_display_name()
        self.display_board[7][1] = self.whi_knight_1.get_display_name()
        self.display_board[7][2] = self.whi_bishop_1.get_display_name()
        self.display_board[7][3] = self.whi_queen_1.get_display_name()
        self.display_board[7][4] = self.whi_king_1.get_display_name()
        self.display_board[7][5] = self.whi_bishop_2.get_display_name()
        self.display_board[7][6] = self.whi_knight_2.get_display_name()
        self.display_board[7][7] = self.whi_rook_2.get_display_name()

        # white pawns
        self.display_board[6][0] = self.whi_pawn_1.get_display_name()
        self.display_board[6][1] = self.whi_pawn_2.get_display_name()
        self.display_board[6][2] = self.whi_pawn_3.get_display_name()
        self.display_board[6][3] = self.whi_pawn_4.get_display_name()
        self.display_board[6][4] = self.whi_pawn_5.get_display_name()
        self.display_board[6][5] = self.whi_pawn_6.get_display_name()
        self.display_board[6][6] = self.whi_pawn_7.get_display_name()
        self.display_board[6][7] = self.whi_pawn_8.get_display_name()

        # black back row
        self.display_board[0][0] = self.blk_rook_1.get_display_name()
        self.display_board[0][1] = self.blk_knight_1.get_display_name()
        self.display_board[0][2] = self.blk_bishop_1.get_display_name()
        self.display_board[0][3] = self.blk_queen_1.get_display_name()
        self.display_board[0][4] = self.blk_king_1.get_display_name()
        self.display_board[0][5] = self.blk_bishop_2.get_display_name()
        self.display_board[0][6] = self.blk_knight_2.get_display_name()
        self.display_board[0][7] = self.blk_rook_2.get_display_name()

        # black pawns
        self.display_board[1][0] = self.blk_pawn_1.get_display_name()
        self.display_board[1][1] = self.blk_pawn_2.get_display_name()
        self.display_board[1][2] = self.blk_pawn_3.get_display_name()
        self.display_board[1][3] = self.blk_pawn_4.get_display_name()
        self.display_board[1][4] = self.blk_pawn_5.get_display_name()
        self.display_board[1][5] = self.blk_pawn_6.get_display_name()
        self.display_board[1][6] = self.blk_pawn_7.get_display_name()
        self.display_board[1][7] = self.blk_pawn_8.get_display_name()

    # return matrix of objects
    def get_board_state(self):
        return self.game_board

    # return matrix of display names
    def get_display_board(self):
        self.game_board[7][0]
        return self.display_board

