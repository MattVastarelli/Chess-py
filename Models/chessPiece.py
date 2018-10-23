class ChessPiece:
    # main chess piece class from which the pieces will inherit
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.name = ""
        self.is_alive = True
        self.valid_moves = list()
        # valid moves are represented as a list of tuples were
        # the first item is the X axis and second the Y axis
        self.is_promoted = False  # for pawn
        self.move_through_piece = False
        # can the piece move to a given spot if its path
        # is obstructed by another piece
        self.first_move = True

    # various getters
    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_valid_moves(self):
        return self.valid_moves

    def get_is_alive(self):
        return self.is_alive

    def get_is_promoted(self):
        return self.is_promoted

    def get_display_name(self):
        # construct the display name
        return self.color + self.name + self.number

    def get_move_through(self):
        # for knight
        return self.move_through_piece

    def is_first_move(self):
        # check if it is the first move
        if self.first_move is True:
            return True
        else:
            return False

    # various setters
    def promote(self):
        # for pawn
        self.is_promoted = True

    def remove_piece(self):
        self.is_alive = False

    def set_first_move(self, t_f):
        self.first_move = t_f


# the inherited piece classes
class Pawn(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Pawn'
        self.valid_moves = [(1, 0)]


class Rook(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Rook'
        self.valid_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)
                            ]


class Knight(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Knight'
        self.move_through_piece = True
        self.valid_moves = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1)]


class Bishop(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Bishop'
        self.valid_moves = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
                            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)
                            ]


class Queen(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Queen'
        self.valid_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
                            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
                            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)
                            ]


class King(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'King'
        self.valid_moves = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (-1, -1), (1, -1)]

