from Controller import game


class GuiHelper:
    # helper class to shorten and simplify the main gui
    def __init__(self):
        self. game = game.Game()
        self.click_count = 0
        self.click_1 = tuple()
        self.click_2 = tuple()

    # This shows that a cell has been clicked and registers the input
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
