
def is_valid_group(group):
    # This function checks if a group (row, column, or square) is valid.
    # A group is valid if it contains each number from 1 to 9 exactly once.
    required_numbers = set(range(1, 10))
    group_numbers = set(group)

    return required_numbers == group_numbers

def main(board):
    # First, we check each row
    for row in board:
        if not is_valid_group(row):
            return 'Try again!'

    # Next, we check each column
    for col_idx in range(9):
        column = []
        for row_idx in range(9):
            column.append(board[row_idx][col_idx])
        if not is_valid_group(column):
            return 'Try again!'

    # check each 3x3 square
    for row in range(0, 9, 3):  # skip by 3 to get to the start of each 3x3 square
        for col in range(0, 9, 3):
            square = []
            for r in range(3): #Iterate over cells squares
                for c in range(3):
                    square.append(board[row + r][col + c])
            if not is_valid_group(square):
                return 'Try again!'

    # If all checks pass, the board is valid
    return 'Finished!'


