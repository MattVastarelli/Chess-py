from Controller import game
from PIL import Image, ImageTk
from Views import guiIcons


class GuiObjects:
    # button class to shorten and simplify the main gui
    def __init__(self):
        self.game = game.Game() # main controller class
        self.click_count = 0
        self.from_spot = tuple()
        self.to_spot = tuple()
        self.icons = guiIcons.GuiIcons()  # icon class
        # hold the memory addresses of the buttons in a matrix
        self.gui_board = [[0 for x in range(8)] for y in range(8)]

    def update(self, to_spot, from_spot):
        self.game.update_board(to_spot, self.game.get_piece(from_spot))
        self.game.update_board(from_spot, 0)

    def look_up_name(self):
        # look up the icon to place
        look_up_name = self.game.get_piece_color(self.from_spot) + self.game.get_piece_type(self.from_spot)

        return self.icons.get_icon(look_up_name)

    # event listener to control the visual movement of a piece
    def event_click(self, row, col):
        self.click_count += 1

        # remember the first click
        if self.click_count is 1:
            self.from_spot = (row, col)
        else:
            # check to see if two clicks have been made
            self.to_spot = (row, col)
            self.click_count = 0

            # call the method to find the move
            move = self.game.find_move_value(self.from_spot, self.to_spot)

            # check to make sure an empty first spot was not selected
            # check for movement to empty spot
            if self.game.spot_is_zero(self.from_spot) is False:
                # check if the piece is the same color as the turn
                if self.game.get_piece_color(self.from_spot) is self.game.get_turn_color():
                    # check to se of the space is empty
                    if self.game.is_spot_occupied(self.to_spot) is False: # movement to open spot is wrong
                        # call the method to check if the move is valid
                        if self.game.is_move_valid(self.from_spot, self.to_spot, move) is True:
                            # check if the move path is valid
                            if self.game.check_valid_move_path(self.from_spot, self.to_spot) is True: # occur error on empty spot , this is the clause
                                if self.game.can_be_promoted(self.from_spot, self.to_spot) is True:
                                    print()

                                look_up_name = self.game.get_piece_color(self.from_spot) + \
                                    self.game.get_piece_type(self.from_spot)

                                # update the board
                                self.update(self.to_spot, self.from_spot)
                                # update the GUI
                                self.gui_board[self.from_spot[0]][self.from_spot[1]].configure(image='', width="20",
                                                                                               height="7")
                                self.gui_board[row][col].configure(image=self.icons.get_icon(look_up_name),
                                                                   width="143", height="110")

                                # flip the turn so the other color could move
                                self.game.filp_trun()
                    else:
                        # check if the color of the selected piece does not match the spot thus can take the piece
                        if self.game.get_piece_color(self.to_spot) is not self.game.get_piece_color(self.from_spot):
                            # check if the move path is valid
                            if self.game.get_piece_type(self.from_spot) is "Pawn":
                                if self.game.check_valid_move_path(self.from_spot, self.to_spot) is True:
                                    # handle the pawn capture case
                                    if self.game.pawn_capture(self.from_spot, self.to_spot) is True:
                                        # take the piece
                                        self.game.take_piece(self.to_spot)

                                        if self.game.can_be_promoted(self.from_spot, self.to_spot):
                                            print()

                                        look_up_name = self.game.get_piece_color(self.from_spot) + \
                                            self.game.get_piece_type(self.from_spot)

                                        # check if the game is over
                                        if self.game.is_game_done(self.to_spot) is True:
                                            print(self.game.get_piece_color(self.from_spot) + " Won")

                                        # update the board
                                        self.update(self.to_spot, self.from_spot)
                                        # update the GUI
                                        self.gui_board[self.from_spot[0]][self.from_spot[1]].configure(image='',
                                                                                                       width="20",
                                                                                                       height="7")
                                        self.gui_board[row][col].configure(image=self.icons.get_icon(look_up_name),
                                                                           width="143", height="110")

                                        # flip the turn so the other color could move
                                        self.game.filp_trun()
                            else:
                                # call the method to check if the move is valid
                                if self.game.is_move_valid(self.from_spot, self.to_spot, move) is True:
                                    # check if the move path is valid
                                    if self.game.check_valid_move_path(self.from_spot, self.to_spot) is True:
                                        # take the piece
                                        self.game.take_piece(self.to_spot)

                                        # check if the game is over
                                        if self.game.is_game_done(self.to_spot) is True:
                                            print(self.game.get_piece_color(self.from_spot) + " Won")

                                        look_up_name = self.game.get_piece_color(self.from_spot) + \
                                            self.game.get_piece_type(self.from_spot)

                                        # update the board
                                        self.update(self.to_spot, self.from_spot)
                                        # update the GUI
                                        self.gui_board[self.from_spot[0]][self.from_spot[1]].configure(image='',
                                                                                                       width="20",
                                                                                                       height="7")
                                        self.gui_board[row][col].configure(image=self.icons.get_icon(look_up_name),
                                                                           width="143", height="110")

                                        # flip the turn so the other color could move
                                        self.game.filp_trun()

            # reset the spot locations
            self.from_spot = (0, 0)
            self.to_spot = (0, 0)
