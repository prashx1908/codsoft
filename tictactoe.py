import random

# Define the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_full(board):
    return " " not in board

# Function to check if the game is over
def is_game_over(board):
    if (board[0] == board[1] == board[2] != " ") or (board[3] == board[4] == board[5] != " ") or (board[6] == board[7] == board[8] != " ") or (board[0] == board[3] == board[6] != " ") or (board[1] == board[4] == board[7] != " ") or (board[2] == board[5] == board[8] != " ") or (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
        return True
    return is_full(board)

# Function to evaluate the board for the AI player
def evaluate(board):
    if (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X"):
        return 1
    elif (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O"):
        return -1
    else:
        return 0

# Minimax algorithm for AI player
def minimax(board, depth, is_maximizing):
    if evaluate(board) == 1:
        return 1
    if evaluate(board) == -1:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make a move for the AI player
def ai_move(board):
    best_move = None
    best_eval = -float('inf')
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = "X"

# Main game loop
while True:
    print_board(board)
    if is_full(board) or is_game_over(board):
        result = evaluate(board)
        if result == 1:
            print("AI wins!")
        elif result == -1:
            print("You win!")
        else:
            print("It's a draw!")
        break
    while True:
        try:
            user_move = int(input("Enter your move (0-8): "))
            if 0 <= user_move <= 8 and board[user_move] == " ":
                board[user_move] = "O"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

    print_board(board)
    if is_full(board) or is_game_over(board):
        result = evaluate(board)
        if result == 1:
            print("AI wins!")
        elif result == -1:
            print("You win!")
        else:
            print("It's a draw!")
        break

    ai_move(board)
