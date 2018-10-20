from Models import chessPiece
from Models import board


class Game:
    # controller class to verify and make the game actions
    def __init__(self):
        self.white_turn = True
        self.black_turn = False
        self.x_axis = 0
        self.y_axis = 0
        # instantiate the board object
        self.board = board.Board()
        self.board.fill_board()

    def is_game_done(self, piece):
        # checks to see if a game is over and who won
        if piece.get_is_alive() is False:
            return piece.get_color() + ' won'

    def find_move_value(self, start_pos, end_pos):
        # find the move distance
        row = end_pos[0] - start_pos[0]
        col = end_pos[1] - start_pos[1]

        move = (row, col)

        return move

    def is_move_valid(self, spot, move):
        # checks to see  if a given move sent as a tuple is valid

        piece = self.board.get_spot(spot[0], spot[1])

        if piece is 0:
            return False
        elif piece.get_name() is "King":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        elif piece.get_name() is "Queen":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        elif piece.get_name() is "Rook":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        elif piece.get_name() is "Knight":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        elif piece.get_name() is "Bishop":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        elif piece.get_name() is "Pawn":
            if move in piece.get_valid_moves():
                return True
            else:
                return False
        else:
            return False
