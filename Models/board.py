from Models import chessPiece


class Board:
    # board class to hold and manage the board state
    def __init__(self):
        # fill the matrix with all 0's to get the correct size
        self.game_board = [[0 for x in range(8)] for y in range(8)]

        # create all the chess pieces
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

    def fill_board(self):
        # build the starting board
        # add the chess pieces to there correct starting

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

    def get_board_state(self):
        # return matrix of objects
        return self.game_board

    def get_spot(self, x, y):
        # return the piece at the given spot
        return self.game_board[x][y]

    def set_spot(self, x, y, piece):
        self.game_board[x][y] = piece

