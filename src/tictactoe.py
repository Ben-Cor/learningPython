# This is a simple Tic Tac Toe game implementation in Python.

# Introductory message
print("Welcome to the Tic Tac Toe game!")
print("This is a two-player game where you will take turns to place your marks on the board.")

# Function to display the game board
def display_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row)) # Join each row with ' | ' for better readability
        print("-" * 13) # Separator line for better readability

# Function to display board called at the start
display_board([[" " for _ in range(4)] for _ in range(4)])

input("Which column do you want to play in? (1-4)?")