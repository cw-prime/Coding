#!/bin/bash
#Lets create a script that would work like a DDOS attack by using a while loop
#In this script we want to contiune to ping our personal pc in a infitine while loop
#Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash
# To End the loop try pressing control z or control c
# Stretch Goal:
# Can you do this with an until loop to have it execute a specfic number of times?



x=1
while [ $x = 1 ]
do
    ping 192.168.0.1
    echo "do you want to run again"
    read x
done

X=1

echo "Please enter an IP to ping.Format (xxx.xxx.xxx.xxx)"
read IpAddress

until [ $X = 7 ]
do
    ping  $IpAddress
    ((X++))
done