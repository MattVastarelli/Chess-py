from Controller import game
from PIL import Image, ImageTk


class GuiHelper:
    # helper class to shorten and simplify the main gui
    def __init__(self):
        self. game = game.Game()
        self.click_count = 0
        self.click_1 = tuple()
        self.click_2 = tuple()
        self.testphoto = Image.open('crown.png')
        self.tkphoto = ImageTk.PhotoImage(self.testphoto)
        # hold the memory addresses of the buttons in a matrix
        self.gui_board = [[0 for x in range(8)] for y in range(8)]

    # event listener to control the visual movement of a piece
    def event_click(self, row, col):
        self.click_count += 1

        # remember the first click
        if self.click_count is 1:
            self.click_1 = (row, col)
        else:
            # check to see if two clicks have been made
            self.click_2 = (row, col)
            self.click_count = 0
            # call the method to find the move
            move = self.game.find_move_value(self.click_1, self.click_2)
            # call the method to check if the move is valid
            self.gui_board[self.click_1[0]][self.click_1[1]].configure(image='', width="20", height="7", )
            self.gui_board[row][col].configure(image=self.tkphoto, width="143", height="110")
