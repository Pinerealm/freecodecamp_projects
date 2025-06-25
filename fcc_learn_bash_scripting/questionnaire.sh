#!/bin/bash

echo -e "\n~~ Questionnaire ~~\n"

QUESTION1="What's your name?"
QUESTION2="Where are you from?"
QUESTION3="What's your favorite coding website?"

echo "$QUESTION1"
read -r NAME

echo "$QUESTION2"
read -r LOCATION

echo "$QUESTION3"
read -r WEBSITE

echo -e "\nHello $NAME from $LOCATION. I learned that your favorite coding website is $WEBSITE!"
