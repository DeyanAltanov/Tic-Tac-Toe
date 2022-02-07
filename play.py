from tic_tac_toe import setup
from tic_tac_toe.helpers import position_maper


def position_validation(position):
    if position in range(1, 10):
        return True
    return False


def position_available(board, position):
    row, col = position_maper[position]
    current_element = board[row][col]
    if not current_element == ' ':
        return False
    return True


def draw_board(board):
    for row in range(len(board)):
        print(f"| {' | '.join(board[row])} |")


def play_turn(board, sign, position):
    if position_available(board, position):
        row, col = position_maper[position]
        board[row][col] = sign
        draw_board(board)
    else:
        current_position = input(f"Please select a valid available position: ")
        current_position = int(current_position)
        play_turn(board, sign, current_position)


def is_row_winner():
    for row in range(len(setup.board)):
        if setup.board[row].count("X") == 3 or setup.board[row].count("O") == 3:
            return True
        return False


def is_col_winner():
    for row in range(len(setup.board)):
        if setup.board[row][0] == setup.board[row][1] == setup.board[row][2] != " ":
            return True
    return False


def is_diag_winner():
    left_diagonal = setup.board[0][0] == setup.board[1][1] == setup.board[2][2] != " "
    right_diagonal = setup.board[0][2] == setup.board[1][1] == setup.board[2][0] != " "
    if left_diagonal or right_diagonal:
        return True
    return False


def has_won():
    if is_row_winner() or is_col_winner() or is_diag_winner():
        return True
    return False


def has_moves(counter):
    if counter < 10:
        return True
    return False


def play():
    turns_counter = 1
    while not has_won() and has_moves(turns_counter):
        current_position = input(f"{setup.player_names[turns_counter % 2]}, select a position [1-9]: ")
        while not current_position.isdigit():
            current_position = input(f"{setup.player_names[turns_counter % 2]}, select a position [1-9]: ")
        current_position = int(current_position)
        while not position_validation(current_position):
            current_position = input(f"{setup.player_names[turns_counter % 2]}, select a position [1-9]: ")
            current_position = int(current_position)
        play_turn(setup.board, setup.player_signs[turns_counter % 2], current_position)
        turns_counter += 1
    print(f"{setup.player_names[(turns_counter - 1) % 2]} has won!")