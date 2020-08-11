# This is importing the random module. It is the equivalent of a code library that we are going to use later on in the code.
import random

#This is our random number generator. It generates a code between and including 1-10.
random_number = random.randint(1, 10)

# This lets us know what the correct number is.
print ("The  secret number is " + str(random_number))

#This prompts us to enter a user name
user_name = input("What should we call you?")

# This Prints out a string with the the username in it>
print("There is a number between 1 & 10. " + user_name + ", if you guess it right you win!")

# This keeps track of the guesses.
guesscount = 0


