# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?


import random



#targetNumber = int(input("Enter the number that need to be guessed (between 0 and 20) only!: "))
targetNumber = random.randint(0, 20)
print(targetNumber)
counter = 0
maxGuesses = 3
while True:
    counter += 1
    myGuess = int(input(f"Guess {counter}: Enter your guess: "))
    if myGuess == targetNumber:
        print(f"Yes! You guessed it in {counter} guesses.")
        break
    print("Guess higher!" if myGuess < targetNumber else "Guess lower!")

    if counter == maxGuesses:
        print(f"You've reached the maximum of {maxGuesses} guesses. Game over!")
        break
        



