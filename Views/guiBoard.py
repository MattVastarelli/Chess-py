import tkinter as tk
import tkinter.messagebox as mb
from Views import guiChessButton
from Views import guiIcons
from Views import saveGamehelper



class GuiBoard:
    # main GUI class to build the gui and launch call the controller methods
    def __init__(self):
        self.top = tk.Tk()
        self.top.title("Chess")
        self.event_new = ''
        self.event_save = ''
        self.event_help = ''
        self.event_about = ''
        self.event_exit = ''
        self.icons = guiIcons.GuiIcons()
        self.white_order = self.icons.white_order()
        self.black_order = self.icons.black_order()
        self.gui_objects = guiChessButton.GuiObjects()

    # This builds the menu
    def build_menu(self, parent):
        menus = (("File", (("New Game", self.event_new),
                      ("Save Game", self.event_save),
                      ("Exit", self.event_exit))),
            ("Help", (("Help", self.event_help),
                      ("About", self.event_about))),)

        menubar = tk.Menu(parent)

        for menu in menus:
            m = tk.Menu(parent)
            for item in menu[1]:
                m.add_command(label=item[0], command=item[1])
            menubar.add_cascade(label=menu[0], menu=m)

        return menubar

    # This is just to represent what we plan to do later, meaningless at this point.
    def function_tabs(self,):
        mb.showinfo("Test", "to be developed later")

    # Saves the game, opens the GUI dialog that performs save game.
    def eventSave(self,):
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

    def show_board(self):
        self.event_new = self.function_tabs
        self.event_save = self.eventSave
        self.event_exit = self.top.destroy
        self.event_help = self.function_tabs
        self.event_about = self.function_tabs

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top)
        ch_board.pack()

        return None

    def run(self):
        self.show_board()
        tk.mainloop()


class LoadGuiBoard(GuiBoard):
    def build_chess_board(self, parent, dictofPieces = None):
        outer = tk.Frame(parent, border=5, relief='sunken')
        inner = tk.Frame(outer)
        inner.pack()
        clr = True
        piecetoplace = False

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
                        if compTuple == key:
                            piecetoplace = True
                            break
                        else:
                            piecetoplace = False
                    if piecetoplace == False:
                        cell = tk.Button(inner, text="", width="20", height="7", background="sandybrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    elif piecetoplace == True:
                        cell = tk.Button(inner, text="", width="143", height="110", background="sandybrown",
                                            image=self.icons.get_icon(dictofPieces.get(compTuple)),
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    clr = False
                elif clr is False:
                    compTuple = (col, row_num)
                    for key in dictofPieces.keys():
                        if compTuple == key:
                            piecetoplace = True
                            break
                        else:
                            piecetoplace = False
                    if piecetoplace == False:
                        cell = tk.Button(inner, text=" ", width="20", height="7", background="saddlebrown",
                                            command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                        cell.grid(row=row, column=col)
                        self.gui_objects.gui_board[row][col] = cell
                    elif piecetoplace == True:
                            cell = tk.Button(inner, text=" ", width="143", height="110", background="saddlebrown",
                                                image=self.icons.get_icon(dictofPieces.get(compTuple)),
                                                command=lambda r=row, c=col: self.gui_objects.event_click(r, c))

                            cell.grid(row=row, column=col)
                            self.gui_objects.gui_board[row][col] = cell
                    clr = True
            row_num += 1

        return outer


    def show_board(self, dictofPieces = None):
        self.event_new = self.function_tabs
        self.event_save = self.eventSave
        self.event_exit = self.top.destroy
        self.event_help = self.function_tabs
        self.event_about = self.function_tabs

        menubar = self.build_menu(self.top)
        self.top["menu"] = menubar
        ch_board = self.build_chess_board(self.top, dictofPieces)
        ch_board.pack()

        return None


    def run(self, dictofPieces = None):
        self.show_board(dictofPieces)
        tk.mainloop()

