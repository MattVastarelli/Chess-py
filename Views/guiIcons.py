from PIL import Image, ImageTk
from collections import deque


class GuiIcons:
    # class to handle the creation and storage of the icons
    # all icons by Freepik https://www.flaticon.com/authors/freepik

    def __init__(self):
        # instantiate all the icons
        # black icons
        self.black_knight_img = Image.open('knight.png')
        self.black_knight = ImageTk.PhotoImage(self.black_knight_img)

        self.black_pawn_img = Image.open('pawn.png')
        self.black_pawn = ImageTk.PhotoImage(self.black_pawn_img)

        self.black_king_img = Image.open('king.png')
        self.black_king = ImageTk.PhotoImage(self.black_king_img)

        self.black_rook_img = Image.open('rook.png')
        self.black_rook = ImageTk.PhotoImage(self.black_rook_img)

        self.black_queen_img = Image.open('queen.png')
        self.black_queen = ImageTk.PhotoImage(self.black_queen_img)

        self.black_bishop_img = Image.open('bishop.png')
        self.black_bishop = ImageTk.PhotoImage(self.black_bishop_img)

        # white icons
        self.white_knight_img = Image.open('knightw.png')
        self.white_knight = ImageTk.PhotoImage(self.white_knight_img)

        self.white_pawn_img = Image.open('pawnw.png')
        self.white_pawn = ImageTk.PhotoImage(self.white_pawn_img)

        self.white_king_img = Image.open('kingw.png')
        self.white_king = ImageTk.PhotoImage(self.white_king_img)

        self.white_rook_img = Image.open('rookw.png')
        self.white_rook = ImageTk.PhotoImage(self.white_rook_img)

        self.white_queen_img = Image.open('queenw.png')
        self.white_queen = ImageTk.PhotoImage(self.white_queen_img)

        self.white_bishop_img = Image.open('bishopw.png')
        self.white_bishop = ImageTk.PhotoImage(self.white_bishop_img)

        # add all the icons to the dictionary
        self.icon_dict = {
                            "WhitePawn": self.white_pawn, "WhiteKnight": self.white_knight,
                            "WhiteKing": self.white_king, "WhiteRook": self.white_rook,
                            "WhiteQueen": self.white_queen, "WhiteBishop": self.white_bishop,
                            "BlackPawn": self.black_pawn, "BlackKnight": self.black_knight,
                            "BlackKing": self.black_king, "BlackRook": self.black_rook,
                            "BlackQueen": self.black_queen, "BlackBishop": self.black_bishop,
                        }

    def black_order(self):
        # black starting order
        black_order = [self.black_rook, self.black_knight, self.black_bishop, self.black_queen, self.black_king,
                       self.black_bishop, self.black_knight, self.black_rook, self.black_pawn, self.black_pawn,
                       self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn,
                       self.black_pawn
                       ]
        black_qeue = deque(black_order)

        return black_qeue

    def white_order(self):
        # white starting order
        white_order = [
                        self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn,
                        self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_rook,
                        self.white_knight, self.white_bishop, self.white_queen, self.white_king, self.white_bishop,
                        self.white_knight, self.white_rook,
                    ]

        white_qeue = deque()

        for item in white_order:
            white_qeue.append(item)

        return white_qeue

    def get_icon(self, name):
        return self.icon_dict[name]