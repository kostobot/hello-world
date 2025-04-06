import random
import time


def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(board[i])}")


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return None

    return "ничья"


def valid_input(board, row, col):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
        return True
    return False


def computer_move(board, player):
    print("Ход компьютера:")
    time.sleep(random.randint(1,3))
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
    move = random.choice(available_moves)
    board[move[0]][move[1]] = player
    print(f"Компьютер выбрал клетку {move[0]} {move[1]}")


def tic_tac_toe():
    board = [['-' for j in range(3)] for i in range(3)]
    player_turn = 'X'
    game_mode = input("Выберите режим игры (2 - для игры с другим игроком, 1 - для игры с компьютером): ").strip()

    while True:
        print_board(board)

        if game_mode == '2' or player_turn == 'X':
            print(f"Ход игрока {player_turn}:")
            try:
                row, col = map(int, input("Введите строку и столбец через пробел (например, 0 1): ").split())
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите два числа.")
                continue

            if valid_input(board, row, col):
                board[row][col] = player_turn
            else:
                print("Эта клетка уже занята или введены некорректные координаты.")
                continue
        else:
            computer_move(board, '0')

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "ничья":
                print("Ничья!")
            else:
                print(f"Игрок {winner} выиграл!")
            break

        player_turn = '0' if player_turn == 'X' else 'X'


tic_tac_toe()