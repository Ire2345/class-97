import random

print("Number Guessing Game")

number=random.randint(1,9)

chances=0

print("Guess a number between(1,9):")

while chances<5:

    guess=int(input("Enter your guess:-"))

    if number==guess: 
        print("you guessed it right")
        break
    elif number<guess:
        print("guess lesser than number")
    else:
         print("guess higher than")
    chances=chances+15
