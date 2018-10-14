# TODO have to handle castling
# TODO need to address that it can only move forward likely through controller
# TODO stop pieces that cant move through others from doing so
# TODO methods for taking a piece, telling if a spot is occupied, getting a piece back, and captured piece list
# TODO the gui has to execute the logic as it may not be able to be sleept /threaded

def main():
    from Models import board
    from Controller import game
    from Views import printHelper
    from Views import GUI

    test_gui =  GUI.tkGui()

    test_gui.show_board()


if __name__ == '__main__':
    main()



