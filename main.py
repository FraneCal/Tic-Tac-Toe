# Tic Tac Toe

board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]


def view_board():
    show_board = [print(row) for row in board]
    return show_board


def user_choice(player_name, marker):
    while True:
        try:
            user_row = int(input(f"{player_name}: Enter row number (between 0 and 2): "))
            user_column = int(input(f"{player_name}: Enter column number (between 0 and 2): "))
            # If the value is below 0 and above 2, raise an error
            if user_row < 0 or user_row > 2 or user_column < 0 or user_column > 2:
                raise ValueError("Out of range.")
            # If the field position is already taken, raise an error
            if board[user_row][user_column] != '_':
                raise ValueError("That position is already taken.")
            # If it's not replace '_' with adequate marking
            board[user_row][user_column] = marker
            return
        except ValueError as err:
            print(f"Invalid input: {err} Please try again.")


def winner_or_draw():

    # (elem == 'X' for elem in row) for row in board
    # The code uses a nested generator expression to iterate over each row and each element in the board

    # all(elem == 'X' for elem in row)
    # The all() function is used to check if all elements in each row are equal to 'X' or 'O'

    # any(all(elem == 'X' for elem in row) for row in board)
    # The any() function is used to check if any of the rows contain only 'X' or 'O'

    row_contains_X = any(all(elem == 'X' for elem in row) for row in board)
    col_contains_X = any(all(row[i] == 'X' for row in board) for i in range(len(board[0])))

    row_contains_0 = any(all(elem == '0' for elem in row) for row in board)
    col_contains_0 = any(all(row[i] == '0' for row in board) for i in range(len(board[0])))


    if row_contains_X or col_contains_X:
        print('X player wins.')
        return True
    elif row_contains_0 or col_contains_0:
        print('0 player wins.')
        return True

    if not any('_' in row for row in board):
        print('Draw')
        return True


while True:
    user_choice("Player 1", "X")
    view_board()
    if winner_or_draw():
        break
    user_choice("Player 2", "0")
    view_board()
    if winner_or_draw():
        break
