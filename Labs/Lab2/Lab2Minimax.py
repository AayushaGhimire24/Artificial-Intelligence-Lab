import math


# Constants
X = 'X'
O = 'O'
EMPTY = ' '


def minimax(board, depth, maximizing_player):
    # Base case: If the game is over or depth limit reached, return the utility value
    if depth == 0 or game_over(board):
        return evaluate(board)
    
    if maximizing_player:
        max_eval = -math.inf
        for move in generate_moves(board, X):
            eval = minimax(move, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in generate_moves(board, O):
            eval = minimax(move, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def game_over(board):
    # Check if the game is over (either someone has won or there are no more moves)
    return check_win(board, X) or check_win(board, O) or not any(EMPTY in row for row in board)


def evaluate(board):
    # Evaluate the current state and return a utility value
    if check_win(board, X):
        return 1  # X wins
    elif check_win(board, O):
        return -1  # O wins
    else:
        return 0  # Draw


def generate_moves(board, player):
    # Generate possible moves from the current board state for a given player
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                new_board = [row[:] for row in board]  # Copy the board
                new_board[i][j] = player
                moves.append(new_board)
    return moves


def check_win(board, player):
    # Check if the player has won
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def main():
    # Initialize an empty board
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and I am O.")
    print("Enter your move by specifying row (0-2) and column (0-2) separated by space.")


    while not game_over(board):
        print_board(board)
        
        # Player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[row][col] = X
        
        if game_over(board):
            break
        
        # AI's move (using minimax algorithm)
        best_move = None
        best_value = -math.inf
        for move in generate_moves(board, O):
            move_value = minimax(move, 3, False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        
        board = best_move
        print_board(board)
    if check_win(board, X):
        print("Congratulations! You win!")
    elif check_win(board, O):
        print("I win!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
