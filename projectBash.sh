#!/bin/bash

API_KEY="282eda0eec2c9b351050d145be9d66"
mycity="Yakutsk"

weather=$(curl -s "http://api.openweathermap.org/data/2.5/weather?q=$mycity&appid=$API_KEY&units=imperial")
temperature=$(echo "$weather" | jq '.main.temp')

if (( $(echo "$temperature > 85" | bc -l) )); then
    message="It's to dam hot for this s**t !!!"
elif (( $(echo "$temperature < 33" | bc -l) )); then
    message="Brick City Grab some Cocoa---."
else
    message="dress to your comfort level"
fi

echo "Current temperature in $mycity: $temperature°F"
echo "$message"
