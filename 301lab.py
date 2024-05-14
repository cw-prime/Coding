# Write a program that works out whether if a given number is an 
# odd or even number
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (number % 2) == 0:
    print("{0} is Even".format(number))
else:
    print("{0} is Odd".format(number))










# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
#age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



import datetime


born = datetime.datetime(1997, 10, 2)

ninety_years_later = born.replace(year=born.year + 90)

now = datetime.datetime.utcnow()

time_left = ninety_years_later - now

years_left = time_left.days // 365  

print(f"You have {years_left} years left until you turn 90.")
