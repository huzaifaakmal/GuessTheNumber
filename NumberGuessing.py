#Generate a random number
#loop 
#Ask the user to make a guess
#Check if enter value is not a number print invalid input
#Check if the number is higher or lower than the generated number
#If the user guesses the number correctly, print a congratulatory message
import random
NumberToGuess=random.randint(1,100)

while True:
    try:
        Guess=int(input("Guess A Number between 1-100 :"))
        if Guess<NumberToGuess:
            print("The Number is too low")
        elif Guess>NumberToGuess:
            print("The Number is too high")
        else:
            print("Congratulations You guessed the number correctly")
            break
    except ValueError:
        print("Please Input Valid Number ")




