# This is a simple Tic Tac Toe game implementation in Python.

# Introductory message
print("Welcome to the Tic Tac Toe game!")
print("This is a two-player game where you will take turns to place your marks on the board.")

# Function to display the game board
def display_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row)) # Join each row with ' | ' for better readability
        print("-" * 9) # Separator line for better readability

# Function to display board called at the start
# creates 3 empty strings using _ as a throwaway variable, creates 3 lots of these strings in a list comprehension
display_board([[" " for _ in range(3)] for _ in range(3)])

input("Player 1 (X) - Which column do you want to play in? (1-3)?")
