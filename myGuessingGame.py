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

# This is the while loop. While the guess count is equal to or less than 4 you can keep trying.
while guesscount <= 4:

# This is converting the input to an integer and assigning it to the variable.   
    guess = int(input())

# This adds one each time the code is cycled.
    guesscount += 1

# This is the comparison operator.
    if guess > random_number:
        print("Try again, it's too high")
    if guess < random_number:
        print("Try again, it's too low!")
    if guess == random_number:

# This keyword ends the loop.
        break

# This compares the guess to the random number.
if guess != random_number:
    print("Ahh, you didn't get it. The number was given to you! lol It was " + str(random_number))
            
# If it's the random number then print this.
else:
    print('You got it in ' + str(guesscount) + ' tries!')


