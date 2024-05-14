# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:

import random

choices = ["rock", "paper", "scissors"]

def play_game():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        while user_choice not in choices:
            user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

print("Thanks for playing!")

play_game()
