#  File: Deal.py
#  Description: HW 10. Monty Hall Problem
#  Student's Name: Mengyuan Dong
#  Student's UT EID: md42252
#  Identifier: BabyElephant
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 10/22
#  Date Last Modified: 10/23


import random

def roll(n):
    return random.randint(1,n)

def runOneTrial():
    prize = roll(3)
    guess = roll(3)
    
    if prize == guess:
        view = roll(3)
        while view == prize:
            view = roll(3)
    else:
        view = roll(3)
        while view == prize or view == guess:
            view = roll(3)

    newGuess = roll(3)
    while newGuess == guess or newGuess == view:
        newGuess = roll(3)

    print (" ",prize,"    ",guess,"    ",view,"      ",newGuess)

    if newGuess == prize:
        return "win"
    elif newGuess != prize:
        return "lose"
    
def main():
    print (" ")
    num = int(input("How many trials do you want to run? "))
    print (" ")
    print ("Prize  Guess  View  New Guess")

    i = 1
    win = 0
    for i in range(1,num+1):
        x = runOneTrial()
        
        if x == "win":
            win += 1
        i += 1
        
    probWin = win / num
    probLose = 1 - probWin

    print(" ")
    print("Probability of winning if you switch =",probWin)
    print("Probability of winning if you do not switch =",probLose)

main()
    

