# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.


a = 23
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a != b:
  print("a not equal b")
elif a <= b:
  print("a is less than")  
elif a > b:
  print("a is greater than")
elif a >= b:
  print("a is greater than or equal to b")
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Create an if statement with two conditions by using or between conditions.
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# Create a nested if statement.
a = int(input("Enter a Number"))
# Create a nested if statement.
b = int(input("Enter a Number"))

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
   
# Hint:  a = int(input("Enter a number "))