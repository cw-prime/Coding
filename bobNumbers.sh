#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
 
#Main
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)

echo "enter a number"
read input
if [ $input -ge 2 ] && [ $input -le 5 ]
   then echo "Valid Number!"
elif [ $input -le 2 ] | [ $input -ge 5 ]
   then echo "not valid"
fi