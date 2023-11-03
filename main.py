from art import logo

# Initialize the board
board = [' ' for _ in range(9)]


# Function to print the board
def print_board(board):
    print(' | '.join(board[:3]))
    print('---------')
    print(' | '.join(board[3:6]))
    print('---------')
    print(' | '.join(board[6:9]))


# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False


# Function to play the game
def tic_tac_toe():
    player = 'X'
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif ' ' not in board:
                    print_board(board)
                    print("It's a tie!")
                    break
                player = 'O' if player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")


# Prints the Logo
print(logo)

# Start the game
tic_tac_toe()
