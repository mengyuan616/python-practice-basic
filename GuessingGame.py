#  File: GuessingGame.py
#  Description: HW7. This program is designed to let the user to play a guessing game.
#  Student's Name: Mengyuan Dong
#  Student's UT EID: md42252
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 10/01
#  Date Last Modified:10/01

def main():

    print (" ")

    print ("Welcome to the guessing game. You have ten tries to guess my number.")
    number = int(input("Please enter your guess: "))

    if number == 1458:
        print ("That's correct!")
        print("Congratulations! You guessed it on the first try!")

    else:
        x = 1
                
        while x < 10:
            
            while number <= 0 or number >= 10000:
                print ("Your guess must be between 0001 and 9999.")
                number = int(input("Please enter a valid guess: "))
                
            if number < 1458:
                print ("Your guess is too low.")
                print ("Guesses so far:",x)
                number = int(input("Please enter your guess: "))
                x = x + 1

            elif number > 1458:
                print ("Your guess is too high.")
                print ("Guesses so far:",x)
                number = int(input("Please enter your guess: "))
                x = x + 1

            elif number == 1458:
                print ("That's correct!")
                print ("Congratulations! You guessed it in",x,"guesses.")
                x = x + 10
                
        if x == 10:
            if number == 1458:
                print ("That's correct!")
                print ("Congratulations! You guessed it in",x,"guesses.")

            else:
                print ("Game over: you ran out of guesses.")
            
main()
