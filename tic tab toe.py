
def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("--+---+--")
    print()


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        print("Player", player, "'s turn")

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Try again.")
            continue

        if board[row][col] != " ":
            print("That position is already occupied!")
            continue

        board[row][col] = player
        moves += 1

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


tic_tac_toe()
