#!/bin/bash

# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is
untilCount=0

until [ $untilCount -gt 10 ]
do
  echo This is number: $untilCount
  ((untilCount++))

done