# TODO have to handle castling
# TODO stop pieces that cant move through others from doing so
# TODO methods for taking a piece, telling if a spot is occupied, getting a piece back, and captured piece list
# TODO need way of refreshing the gui or just one spot


def main():
    from Views import GUI

    test_gui = GUI.TkGui()
    test_gui.run()


if __name__ == '__main__':
    main()



