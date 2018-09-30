# TODO have to handle castling
# TODO need to address that it can only move forward likely through controller
# TODO have some way of tracking the location of a given piece likely dict of tuples and spot to piece
# TODO methods for taking a piece, telling if a spot is occupied, getting a piece back, and captured piece list
# TODO setters to model / game to change values ie set a piece as captured


def main():
    from Models import board
    from Controller import game
    from Views import printHelper

    test_game = game.Game()
    test_board = board.Board()
    test_board.fill_board()

    printHelper.print_board(test_board.get_board_state())


if __name__ == '__main__':
    main()



