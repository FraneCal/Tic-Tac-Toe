board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def view_board():
    for row in board:
        print(row)

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

    # Check rows for wins
    for row in board:
        if all(elem == 'X' for elem in row):
            print('X player wins.')
            return True
        elif all(elem == 'O' for elem in row):
            print('O player wins.')
            return True

    # Check columns for wins
    for i in range(len(board[0])):
        if all(row[i] == 'X' for row in board):
            print('X player wins.')
            return True
        elif all(row[i] == 'O' for row in board):
            print('O player wins.')
            return True

    # Check diagonals for wins
    if all(board[i][i] == 'X' for i in range(len(board))) or all(board[i][len(board)-i-1] == 'X' for i in range(len(board))):
        print('X player wins.')
        return True
    elif all(board[i][i] == 'O' for i in range(len(board))) or all(board[i][len(board)-i-1] == 'O' for i in range(len(board))):
        print('O player wins.')
        return True

    if not any('_' in row for row in board):
        print('Draw')
        return True

while True:
    view_board()
    user_choice("Player 1", "X")
    view_board()
    if winner_or_draw():
        break
    user_choice("Player 2", "O")
    if winner_or_draw():
        break
