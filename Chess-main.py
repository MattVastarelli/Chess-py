from Models import chessPiece
from Controller import game

# TODO have to handle castling
# TODO need to address that it can only move forward likely through controller
# TODO have some way of tracking the location of a given piece likely dict of tuples and spot to piece
# TODO methods for taking a piece, telling if a spot is occupied, getting a piece back, and captured piece list
# TODO setters to model / game to change values ie set a piece as captured

testGame = game.Game()
testGame.fill_board()
testGame.make_display_board()

'''
for item in testGame.get_board_state()[1][0]:
    print(chessPiece.)
'''


def printMatrix(testMatrix):
    for row in testGame.get_display_board():
        print(row)


#printMatrix(testGame.get_display_board())

#print(testGame.get_board_state())

def printMatrix1(testMatrix):
    for item in testMatrix:
        if item[0] == 0:
            print(0)
        else:
            print(item[0].get_display_name()) #need not make shure that there is an object at a given location


printMatrix1(testGame.get_board_state())