import tkinter as Chess
import tkinter.messagebox as mb

top = Chess.Tk()
# This builds the menu


def buildMenu(parent):
    menus = (
        ("File", (("New Game", eventNew),
            ("Resume Game", eventResume),
            ("Save Game", eventSave),
            ("Exit", eventExit))),
            ("Help", (("Help", eventHelp),
            ("About", eventAbout))),
    )

    menubar = Chess.Menu(parent)

    for menu in menus:
        m = Chess.Menu(parent)
        for item in menu[1]:
            m.add_command(label = item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu = m)

    return menubar


# This shows that a cell has been clicked and registers the input
def eventClick (row, col):
    mb.showinfo("cells", "Cell Clicked: rows:{}, col:{}".format(row,col))


# This is just to represent what we plan to do later, meaningless at this point.
def Functiontabs():
    mb.showinfo("Test", "to be developed later")


# We build the chess board
def buildChessBoard (parent):
    outer = Chess.Frame(parent,border=5, relief='sunken')
    inner = Chess.Frame(outer)
    inner.pack()
    clr = True
    for row in range(8): # This for loop builds the board while also alternating black and white squares
        if row%2 == 0:
            clr = True
        if row%2 != 0:
            clr = False
        for col in range(8):
            if clr == True:
                cell = Chess.Button(inner,text=" ", width="20", height="7", background = "white",
                    command= lambda r=row, c=col: eventClick(r, c))

                cell.grid(row=row, column =col)
                clr = False
            elif clr == False:
                cell = Chess.Button(inner,text=" ", width="20", height="7", background = "black",
                    command= lambda r=row, c=col: eventClick(r, c))

                cell.grid(row=row, column = col)
                clr = True

    return outer


eventNew = Functiontabs
eventResume = Functiontabs
eventSave = Functiontabs
eventExit = top.quit
eventHelp = Functiontabs
eventAbout = Functiontabs

menubar = buildMenu(top)
top["menu"] = menubar
chBoard = buildChessBoard(top)
chBoard.pack()

Chess.mainloop()