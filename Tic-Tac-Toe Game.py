def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("=== Tic-Tac-Toe ===")
    print("Player X vs Player O")
    print("Enter row and column numbers (1-3) to place your mark.")

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter col (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("⚠️ Invalid input. Row and column must be 1-3.")
                continue

            if board[row][col] != " ":
                print("⚠️ Cell already taken. Choose another.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("🤝 It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
