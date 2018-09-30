# helper functions to print useful information


# print the matrix
def print_board(matrix):
    for i in range(0, len(matrix), 1):
        print()
        for j in range(0, len(matrix), 1):
            # check to only call class functions of members of the class
            if matrix[i][j] is 0:
                print(0, end=' ')
            else:
                print(matrix[i][j].get_display_name(), end=' ')