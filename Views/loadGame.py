from tkinter import *
import tkinter.messagebox as mb


class LoadFromFile:
    # Constructor for LoadFromFIle
    def __init__(self, game_instance):
        self.loadGame = Tk()
        self.loadGame.geometry("200x115")
        self.loadGame.title("Load Game")
        self.loadGame.resizable(0, 0)
        self.load_save = ''
        self.event_cancel = ''
        self.text_box = ''
        self.dictofpieces = dict()
        self.game = game_instance
        self.turn = ""

    def __repr__(self):
        # Returns a dictionary as a string to the caller.
        return str(self.dictofpieces)

    def build_load_game(self, parent):
        # This method builds the frame that takes the file input from the user
        frame1 = Frame(self.loadGame)
        frame1.pack(expand=True)

        for i in range(3):
            if i == 0:
                self.text_box = Entry(frame1)
                self.text_box.pack()
            if i == 1:
                load_button = Button(frame1, text="Load Game", width="9", height="1", command=self.load_save)
                load_button.pack(side=LEFT)
            if i == 2:
                cancel_button = Button(frame1, text="Cancel", width="9", height="1", command=self.event_cancel)
                cancel_button.pack(side=RIGHT)

    def load_from_file(self):
        # This method takes the file name entered by the user, and opens it and loads the data from it.
        text1 = self.text_box.get()
        if text1 == '':  # If no file name is entered, we display a message
            mb.showinfo("ERROR!", "File name required!")
            self.loadGame.destroy()
        # Otherwise we read in from the file and a create a dictionary of all pieces and the turn.
        else:
            text1 += ".txt"
            try:
                x = -1
                y = -1
                counter = 0
                color = ''
                piece = ''
                number_holder = ''
                test = [line.strip() for line in open(text1, 'r')]
                for line in test:
                    if line == "White" or line == "Black":
                        self.turn = line
                    else:
                        for c in line:
                            if c.isdigit() and y == -1:
                                y = int(c)
                            elif c.isdigit() and x == -1:
                                x = int(c)
                            elif x != -1 and y != -1:
                                number_holder += str(x)
                                number_holder += str(y)
                                x = -1
                                y = -1
                            elif c == '@' and counter == 0:
                                counter += 1
                            elif c != '@' and counter == 1 and c.isalpha():
                                color += c
                            elif c == '@' and counter == 1:
                                counter += 1
                            elif c != '@' and counter == 2 and c.isalpha():
                                piece += c

                        totPiece = color+piece
                        self.dictofpieces[number_holder] = totPiece
                        piece = ''
                        color = ''
                        counter = 0
                        number_holder = ''
                        if y != -1 or x != -1:
                            y = -1
                            x = -1
                self.dictofpieces["turn"] = self.turn
                self.loadGame.quit()
            except FileNotFoundError:  # in case file not found.
                mb.showinfo("ERROR", "File Does Not Exist!")
                self.loadGame.destroy()

    def destroy_windows(self):
        self.loadGame.destroy()
        return None

    def show_load_game(self):
        # This method builds the main didsplay and creates the event handler associations.
        self.load_save = self.load_from_file
        self.event_cancel = self.loadGame.destroy
        self.build_load_game(self.loadGame)

        return None

    def run_load(self):
        # Here we run the mainloop that displays the content on the screen.
        self.show_load_game()
        self.loadGame.mainloop()
