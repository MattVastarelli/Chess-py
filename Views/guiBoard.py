import tkinter as tk
import tkinter.messagebox as mb
from Controller import guiChessButton
from Models import guiIcons
from Views import saveGamehelper
from Views import newgamehelper
from Views import helpHelper


class GuiBoard:
    # main GUI class to build the gui and launch call the controller methods
    def __init__(self):
        self.top = tk.Tk()
        self.top.title("Chess")
        self.event_new = ''
        self.event_help = ''
        self.event_about = ''
        self.event_exit = ''
        self.save = ''
        self.icons = guiIcons.GuiIcons()
        self.white_order = self.icons.white_order()
        self.black_order = self.icons.black_order()
        self.gui_objects = guiChessButton.GuiObjects()

    # This builds the menu
    def build_menu(self, parent):
        menus = (("File", (("New Game", self.event_new),
                      ("Save Game", self.event_save),
                      ("Exit", self.event_exit))),
            ("Help", (("Help", self.help),
                      ("About", self.about))),)

        menubar = tk.Menu(parent)
        # This for loop populates the loop with the commands.
        for menu in menus:
            m = tk.Menu(parent)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            menubar.add_cascade(label=menu[0], menu=m)

        return menubar

    def about(self):
        mb.showinfo("About", "Authors: Matthew and Evan")

        return None

    def help(self,):
        run_help = helpHelper.Help()
        run_help.run()

    def event_save(self,):
        # Saves the game, opens the GUI dialog that performs save game.
        esgui = saveGamehelper.SaveToFile(self.gui_objects.game)
        esgui.run_save()

    def build_saved_board(self, dict):
        # the code to build the board after it is read in from the file
        return None

    # build the chess board
    def build_chess_board(self, parent):
        outer = tk.Frame(parent, border=5, relief='sunken')
        inner = tk.Frame(outer)
        inner.pack()
        clr = True

        row_num = 0
        # This for loop builds the board while also alternating sandybrown and saddlebrown squares
        for row in range(8):
            if row % 2 == 0:
                clr = True
            if row % 2 != 0:
                clr = False
            for col in range(8):
                if clr is True:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    else:
                        if row_num <= 1:
                            # black side
                            cell = tk.Button(inner, text="", width="143", height="110", background="sandybrown",
                                             image=self.black_order.popleft(),
                                             command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                            cell.grid(row=row, column=col)
                            self.gui_objects.gui_board[row][col] = cell
                        else:
                            # white side
                            cell = tk.Button(inner, text="", width="143", height="110", background="sandybrown",
                                             image=self.white_order.popleft(),
                                             command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                            cell.grid(row=row, column=col)
                            self.gui_objects.gui_board[row][col] = cell
                    clr = False
                elif clr is False:
                    if row_num > 1 and row_num < 6:
                        cell = tk.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    else:
                        if row_num <= 1:
                            # black side
                            cell = tk.Button(inner, text=" ", width="143", height="110", background="saddlebrown",
                                             image=self.black_order.popleft(),
                                             command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                            cell.grid(row=row, column=col)
                            self.gui_objects.gui_board[row][col] = cell
                        else:
                            # white side
                            cell = tk.Button(inner, text=" ", width="143", height="110", background="saddlebrown",
                                             image=self.white_order.popleft(),
                                             command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                            cell.grid(row=row, column=col)
                            self.gui_objects.gui_board[row][col] = cell

                    clr = True
            row_num += 1
        return outer

    def new_game(self):
        # Calls a new game, if the user would like to start over.
        nggui = newgamehelper.NewGame(self.top)
        nggui.run()

    def show_board(self):
        # Creates the event handling associations and the creates tk.top and makes it ready to be displayed.
        self.event_new = self.new_game
        self.save = self.event_save
        self.event_exit = self.top.destroy

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top)
        ch_board.pack()

        return None

    def run(self):
        # This is the main loop
        self.show_board()
        tk.mainloop()


class LoadGuiBoard(GuiBoard):
    # This class inherits GuiBoard, this allows for a game to be resumed from a file.
    # constructor
    def __init__(self):
        GuiBoard.__init__(self)
        self.currentTurn = ""

    def build_chess_board(self, parent, dictofPieces=None):
        # This builds the chess board, it takes the dictionary from splash screen.
        outer = tk.Frame(parent, border=5, relief='sunken')
        inner = tk.Frame(outer)
        inner.pack()
        clr = True
        piece_to_place = False
        turnfound = False

        row_num = 0
        # This for loop builds the board while also alternating sandybrown and saddlebrown squares
        for row in range(8):
            if row % 2 == 0:
                clr = True
            if row % 2 != 0:
                clr = False
            for col in range(8):
                if clr is True:
                    compTuple = (col, row_num)
                    for key in dictofPieces.keys():
                        # We check if a piece is to be placed, we compare key from dictionary
                        # to current coordinates generated by our loop
                        if compTuple == key:
                            piece_to_place = True
                            break
                        # Here we check for the turn, once found, we assign the turn.
                        elif key == "turn" and turnfound == False:
                            turnfound = True
                            if dictofPieces.get(key) == "turnWhite":
                                self.currentTurn = "White"
                            elif dictofPieces.get(key) == "turnBlack":
                                self.currentTurn = "Black"
                            game = self.gui_objects.get_game()
                            game.set_turn_color(self.currentTurn)
                        # Otherwise we set to false.
                        else:
                            piece_to_place = False

                    if piece_to_place is False:
                        # don't place the icon on the board
                        cell = tk.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    elif piece_to_place:
                        # place the icon on the board
                        cell = tk.Button(inner, text="", width="143", height="110", background="sandybrown",
                                            image=self.icons.get_icon(dictofPieces.get(compTuple)),
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                        # initiate the correct piece on the given spot in the board matrix
                        game = self.gui_objects.get_game()
                        spot = (row, col)
                        game.promote_and_resume(spot, dictofPieces.get(compTuple))
                    clr = False
                elif clr is False:
                    compTuple = (col, row_num)
                    for key in dictofPieces.keys():
                        if compTuple == key:
                            piece_to_place = True
                            break
                        else:
                            piece_to_place = False
                    if piece_to_place is False:
                        # don't place the icon on the board
                        cell = tk.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                         command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    elif piece_to_place:
                        # place the icon on the board
                        cell = tk.Button(inner, text=" ", width="143", height="110", background="saddlebrown",
                                         image=self.icons.get_icon(dictofPieces.get(compTuple)),
                                         command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                        # initiate the correct piece on the given spot in the board matrix
                        game = self.gui_objects.get_game()
                        spot = (row, col)
                        game.promote_and_resume(spot, dictofPieces.get(compTuple))
                    clr = True
            row_num += 1

        return outer

    def which_turn(self):
        # We display a message of what turn it is, so the user knows.
        if self.currentTurn == "White":
            mb.showinfo("Info", "It's White's Turn!")
        elif self.currentTurn == "Black":
            mb.showinfo("Info", "It's Black's Turn!")

        return None

    def show_board(self, dictofPieces=None):
        # Creates the event handle assignment and allows for the tkinter top level to be created and packed.
        self.event_new = self.new_game
        self.save = self.event_save
        self.event_exit = self.top.destroy
        self.event_help = self.help
        self.event_about = self.about

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top, dictofPieces)
        ch_board.pack()

        return None

    def run(self, dictofPieces=None):
        # This runs the display and gets mainloop going.
        print(dictofPieces)
        self.show_board(dictofPieces)
        self.which_turn()
        tk.mainloop()
