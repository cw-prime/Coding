#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/
echo "how is your day going (good/bad)"
read mood
case $mood in


  great | amazing | awesome!)
    echo "thats good to hear your day is $mood"
    ;;

  terrible)
    echo "sorry to hear your day is $mood"
    ;;

  fine)
    echo " so you days are $mood"
    ;;

  *)
    echo "unknown mood"
    ;;
esac

