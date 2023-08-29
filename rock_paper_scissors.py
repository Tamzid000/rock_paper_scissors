import tkinter as tk
from tkinter import messagebox
import random

# Function to check the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle player choice
def make_choice(choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create buttons for player's choice
rock_button = tk.Button(root, text="Rock", command=lambda: make_choice("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: make_choice("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: make_choice("scissors"))

# Place buttons on the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Start the Tkinter main loop
root.mainloop()