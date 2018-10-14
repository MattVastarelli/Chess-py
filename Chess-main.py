# TODO have to handle castling
# TODO stop pieces that cant move through others from doing so
# TODO methods for taking a piece, telling if a spot is occupied, getting a piece back, and captured piece list


def main():
    from Models import board
    from Controller import game
    from Views import printHelper
    from Views import GUI

    test_gui = GUI.TkGui()

    test_gui.show_board()


if __name__ == '__main__':
    main()



