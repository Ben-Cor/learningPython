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

player_choice = input("Player 1 (X) - Which column do you want to play in? (1-3)?")
if player_choice == "1":
    print("You chose column 1")
elif player_choice == "2":
    print("You chose column 2")
elif player_choice == "3":
    print("You chose column 3")