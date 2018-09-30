class ChessPiece:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.name = ""
        self.is_alive = True
        # valid moves are represented as a list of tuples were
        # the first item is the X axis and second the Y axis
        self.valid_moves = list()
        self.is_promoted = False  # for pawn only
        # can the piece move to a given spot if its path
        # is obstructed by another piece
        self.move_through_piece = False

    # various getters
    def get_name(self):
        return self.name

    def get_display_name(self):
        return self.color + self.name + str(self.number)

    def get_color(self):
        return self.color

    def get_valid_moves(self):
        return self.valid_moves

    def get_is_alive(self):
        return self.is_alive

    def get_is_promoted(self):
        return self.is_promoted

    def get_display_name(self):
        return self.color + self.name + self.number

    def get_move_through(self):
        return self.move_through_piece

    # various setters
    def promote(self):
        self.is_promoted = True

    def remove_piece(self):
        self.is_alive = False


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
                            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]


class Knight(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Knight'
        self.move_through_piece = True
        self.valid_moves = [(1, 2), (2, 1)]


class Bishop(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Bishop'
        self.valid_moves = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]


class Queen(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'Queen'
        self.valid_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]


class King(ChessPiece):
    def __init__(self, color, number):
        ChessPiece.__init__(self, color, number)
        self.name = 'King'
        self.valid_moves = [(1, 0), (0, 1), (1, 1)]

