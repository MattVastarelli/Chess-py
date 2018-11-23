from tkinter import *
import tkinter.messagebox as mb


class SaveToFile:
    # Save to file constructor
    def __init__(self, game_instance):
        self.saveGame = Tk()
        self.saveGame.geometry("200x115")
        self.saveGame.title("Save Game")
        self.saveGame.resizable(0, 0)
        self.event_save = ''
        self.event_cancel = ''
        self.text_box = ''
        self.game = game_instance

    def __repr__(self):
        # Returns a string for the filename
        return str(self.filename)

    def build_save_game(self, parent):
        # this function build the frame
        frame1 = Frame(self.saveGame)
        frame1.pack(expand=True)
        
        for i in range(3):
            if i == 0:
                self.text_box = Entry(frame1)
                self.text_box.pack()
            if i == 1:
                save_button = Button(frame1, text="Save Game", width="9", height="1", command=self.event_save)
                save_button.pack(side=LEFT)
            if i == 2:
                cancel_button = Button(frame1, text="Cancel", width="9", height="1", command=self.event_cancel)
                cancel_button.pack(side=RIGHT)

    def readout_file(self):
        # readout function gets test typed in by user
        text1 = self.text_box.get()
        if text1 == '':  # if no entry, error displayed
            mb.showinfo("ERROR!", "You must type in a name!")
            self.saveGame.destroy()
        # if entry we append .txt to make it a test file,
        # then we read out the piece color, position, type and current turn to a file
        else:
            text1 += ".txt"
            fn = open(text1, 'w')
            x = 0
            y = 0
            while y <= 7:
                while x <= 7:
                    tuple1 = (x, y)
                    x += 1
                    occupied = self.game.is_spot_occupied(tuple1)

                    if occupied:
                        piece = self.game.get_piece_type(tuple1)
                        color = self.game.get_piece_color(tuple1)
                        tofile = str(tuple1)
                        tofile += '@'
                        color = str(color)
                        tofile += color
                        tofile += '@'
                        piece = str(piece)
                        tofile += piece
                        fn.write(tofile)
                        fn.write('\n')
                    
                    elif not occupied:
                        continue
                x = 0
                y += 1
            fn.write(str(self.game.get_turn_color()))
            fn.write('\n')
            fn.write('\n')
            fn.close()
            self.saveGame.destroy()

        return None

    def show_save_game(self):
        # This creates the main display
        self.event_save = self.readout_file
        self.event_cancel = self.saveGame.destroy
        sg = self.build_save_game(self.saveGame)

        return None

    def run_save(self):
        # This runs the GUI
        self.show_save_game()
        self.saveGame.mainloop()
