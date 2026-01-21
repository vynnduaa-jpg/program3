import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board):
    while True:
        try:
            move = int(input("Masukkan posisi (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Posisi tidak valid atau sudah terisi.")
        except ValueError:
            print("Masukkan angka antara 1-9.")

def computer_move(board):
    available = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if available:
        row, col = random.choice(available)
        board[row][col] = "O"
        print(f"Komputer memilih posisi {row*3 + col + 1}")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Selamat datang di Tic Tac Toe!")
    print("Anda adalah X, komputer adalah O.")
    print("Papan:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board):
            print("Selamat! Anda menang!")
            break
        if is_full(board):
            print("Seri!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board):
            print("Komputer menang!")
            break
        if is_full(board):
            print("Seri!")
            break

if __name__ == "__main__":
    main()