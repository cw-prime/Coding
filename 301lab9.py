# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# You will need to use a for loop to write this:


#Write your code below this row 👇


# FizzBuzz Program

for number in range(1, 101):  # Loop from 1 to 100
    if number % 15 == 0:  # Check if number is divisible by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Check if number is divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # Check if number is divisible by 5
        print("Buzz")
    else:
        print(number)  # Print the number if none of the above conditions are true
