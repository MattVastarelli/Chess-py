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
            return True

    def get_turn_color(self):
        if self.white_turn is True:
            return "White"
        else:
            return "Black"

    def get_piece_color(self, spot):
        # get the color of a piece on a given spot
        piece = self.board.get_spot(spot[0], spot[1])
        return piece.get_color()

    def filp_trun(self):
        # change turn after move
        self.white_turn = not self.white_turn
        self.black_turn = not self.black_turn

    def find_move_value(self, start_pos, end_pos):
        # find the move distance
        row = end_pos[0] - start_pos[0]
        col = end_pos[1] - start_pos[1]

        move = (row, col)
        return move

    def update_board(self, spot, piece):
        # update the board with the move
        self.board.set_spot(spot[0], spot[1], piece)

    def is_spot_full(self, x, y):
        # check if there is a piece on a spot
        print(x)

    def is_move_valid(self, from_spot, to_spot, move):
        # checks to see  if a given move sent as a tuple is valid
        piece = self.board.get_spot(from_spot[0], from_spot[1])
        # TODO remove piece and place in list need to save from garbage collector
        # TODO method to get a piece back
        print(piece.get_display_name() + "From: " + str(from_spot) + " To: " + str(to_spot))
        if piece is 0:
            return False
        elif piece.get_name() is "Pawn":
            # handle the pawn case
            if piece.is_first_move():
                if piece.get_color() is "White":
                    if move in [(-2, 0), (-1, 0)]:
                        self.update_board(to_spot, piece)
                        self.update_board(from_spot, 0)
                        piece.set_first_move(False)
                        return True
                    else:
                        return False
                else:
                    if move in piece.get_valid_moves() or [(2, 0)]:
                        self.update_board(to_spot, piece)
                        self.update_board(from_spot, 0)
                        piece.set_first_move(False)
                        return True
                    else:
                        return False
            else:
                if piece.get_color() is "White":
                    if move == (-1, 0):
                        self.update_board(to_spot, piece)
                        self.update_board(from_spot, 0)
                        return True
                    else:
                        return False
                else:
                    if move in piece.get_valid_moves():
                        self.update_board(to_spot, piece)
                        self.update_board(from_spot, 0)
                        return True
                    else:
                        return False
        elif move in piece.get_valid_moves():
            self.update_board(to_spot, piece)
            self.update_board(from_spot, 0)
            return True
        else:
            return False

