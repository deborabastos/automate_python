#! /usr/bin/env python3
# Shebang Line tells your computer that you want to run the script using pyhton3

# This is a guess the number game
import random
print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
	print('Take a guess. You have 6 chances!')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break # This condition is for the correct guess.

if guess ==  secretNumber:
	print('Good job, ' + name + '! You guessed my secret number (' + str(secretNumber) + ') in ' + str(guessesTaken) + ' guesses')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))