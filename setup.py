def setup():
    global player_1_name, player_2_name
    global board
    board = [[" ", " ", " "]for _ in range(3)]
    player_1_name = input("Enter Player 1 Name: ")
    player_2_name = input("Enter Player 2 Name: ")
    player_1_sign = input(f"{player_1_name}, please select a sign - X, or O: ")
    while player_1_sign.lower() not in ('x', 'o'):
        player_1_sign = input(f"{player_1_name}, please select a sign - X, or O: ")
    player_1_sign = player_1_sign.upper()
    player_2_sign = 'O' if player_1_sign == 'X' else 'X'
    global player_signs, player_names
    player_signs = {1: player_1_sign, 0: player_2_sign}
    player_names = {1: player_1_name, 0: player_2_name}
    print("This is the numeration of the board: ")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print("Player 1 starts first!")