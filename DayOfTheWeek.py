#  File: DayOfTheWeek.py
#  Description: HW 6. This program is designed to output the day of the week for the date entered.
#  Student's Name: Mengyuan Dong
#  Student's UT EID: md42252
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 09/27
#  Date Last Modified: 09/28

def main():

    #Create an empty line
    print(" ")

    #Ask for a date (day, month and year)
    year = int(input("Please enter the year (an integer): "))
    a = month = str(input("Please enter the month (a string): "))
    b = day = int(input("Please enter the day (an integer): "))

    #Define c and d
    if a == "January" or month == "February":
        year = year - 1 

        c = year % 100
        d = year // 100
        
    else:
        c = year % 100
        d = year // 100

    #Define a
    if a == "January":
        a = 11
    elif a == "February":
        a = 12
    elif a == "March":
        a = 1
    elif a == "April":
        a = 2
    elif a == "May":
        a = 3
    elif a == "June":
        a = 4
    elif a == "July":
        a = 5
    elif a == "August":
        a = 6
    elif a == "September":
        a = 7
    elif a == "October":
        a = 8
    elif a == "November":
        a = 9
    else:
        a = 10

    #Get the day of the week
    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    if r == 0:
        final = "Sunday"
    elif r == 1:
        final = "Monday"
    elif r == 2:
        final = "Tuesday"
    elif r == 3:
        final = "Wednesday"
    elif r == 4:
        final = "Thursday"
    elif r == 5:
        final = "Friday"
    else:
        final = "Saturday"

    print ("The day of the week is",final+".")   

main()
    
