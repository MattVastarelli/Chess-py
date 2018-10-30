from PIL import Image, ImageTk


class GuiIcons:
    # class to handle the creation and storage of the icons
    # all icons by Freepik https://www.flaticon.com/authors/freepik

    def __init__(self):
        self.icon_dict = dict()  # dictionary to hold the icons

        # instantiate all the icons
        # black icons
        self.black_knight_img = Image.open('knight.png')
        self.black_knight = ImageTk.PhotoImage(self.black_knight_img)

        self.black_pawn_img = Image.open('pawn.png')
        self.black_pawn = ImageTk.PhotoImage(self.black_knight_img)

        self.black_king_img = Image.open('king.png')
        self.black_king = ImageTk.PhotoImage(self.black_knight_img)

        self.black_rook_img = Image.open('rook.png')
        self.black_rook = ImageTk.PhotoImage(self.black_knight_img)

        self.black_queen_img = Image.open('knight.png')
        self.black_queen = ImageTk.PhotoImage(self.black_knight_img)

        self.black_bishop_img = Image.open('bishop.png')
        self.black_knight = ImageTk.PhotoImage(self.black_knight_img)

        # white icons
        self.white_knight_img = Image.open('knightw.png')
        self.white_knight = ImageTk.PhotoImage(self.black_knight_img)

        self.white_pawn_img = Image.open('pawnw.png')
        self.white_pawn = ImageTk.PhotoImage(self.black_knight_img)

        self.white_king_img = Image.open('kingw.png')
        self.white_king = ImageTk.PhotoImage(self.black_knight_img)

        self.white_rook_img = Image.open('rookw.png')
        self.white_rook = ImageTk.PhotoImage(self.black_knight_img)

        self.white_queen_img = Image.open('queenw.png')
        self.white_queen = ImageTk.PhotoImage(self.black_knight_img)

        self.white_bishop_img = Image.open('bishopw.png')
        self.white_knight = ImageTk.PhotoImage(self.black_knight_img)

    def fill_dict(self):
        # add the pieces to the dictionary
        return None

    def black_order(self):
        # black starting order
        return None

    def white_order(self):
        # white starting order
        return None

    def get_icon(self, name):
        return self.icon_dict[name]