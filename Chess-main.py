from Models import chessPiece
from Controller import game

# TODO have to handle castling
# TODO need to address that it can only move forward likely through controller


testGame = game.Game()
testGame.fill_board()
testGame.make_display_board()

'''
for item in testGame.get_board_state()[1][0]:
    print(chessPiece.)
'''
#print(testGame.get_board_state())


def printMatrix(testMatrix):
    for row in testGame.get_display_board():
        print(row)

#print(testGame.get_display_board())
printMatrix(testGame.get_display_board())
