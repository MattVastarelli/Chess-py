from Models import chessPiece
from Models import board


class Game:
    # controller class to verify and make the game actions
    def __init__(self):
        self.white_turn = True
        self.black_turn = False
        self.x_axis = 0
        self.y_axis = 0

    def is_game_done(self, King):
        # checks to see if a game is oven and who won
        if chessPiece.King.is_alive is False:
            return chessPiece.King.get_color() + ' won'

    def find_move_value(self, start_pos, end_pos):
        # find the move distance
        row = end_pos[0] - start_pos[0]
        col = end_pos[1] - start_pos[1]

        move = (row, col)

        return move

    def is_move_valid(self, move):
        # checks to see  if a given move sent as a tuple is valid
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

