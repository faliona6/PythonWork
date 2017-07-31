#Star Project
import math

#Challenge 1 Stairs Left

def challenge_1():
    a = ""
    number = input("Challenge 1 is the stairs on the left. How many rows do you want for Challenge 1?")
    number_int = int(number)

    for stars in range(1, number_int + 1): #counter starts at 1 instead of 0 because we want one star on the first line, 2 stars on second, etc.
        for x in range(stars):
            a = a + "*"
        print(a)
        a = "" #reset so that the next line doesn't add what was already made before.

#Challenge 2 Stairs Right

def challenge_2():
    rows = input("Challenge 2 is the stairs on the right. How many rows do you want for Challenge 2?")
    rows_int = int(rows)

    for stars in range(1, rows_int + 1): # number of rows, start from 1 so that there is 1 star on the frist line
        c = ""
        for x in range(-1 * stars + rows_int): #uses function -x + rows to find number of spaces
            c = c + " "
        for y in range(stars): #the number of stars is the row number it is on, which is called stars
            c = c + "*"
        print(c)

#Challenge 3 Triangle

def challenge_3():
    row = input("Challenge 3 is the triangle. How many rows do you want for Challenge 3?")
    row_int = int(row)

    for stars in range(1, row_int + 1): # of rows
        e = ""
        for x in range(-1 * stars + row_int): # function -x + rows
            e = e + " "
        for y in range(2 * stars - 1): # function 2x - 1, number of rows doesn't affect number of stars per row
            e = e + "*"
        print(e) #print the entire string, then reset to empty string.


#Challenge 4 Diamond

def challenge_4():
    raw = input("Challenge 4 is the diamond. How many rows do you want for Challenge 4? (Odd numbers only!)")
    raw_int = int(raw) #set the input as an integer 'raw'
    fullraw_int = raw_int #to save a copy of the actual integer, set var fullraw_int equal to input value
    raw_int = raw_int//2 #because the image is split into half, disregarding 1 line in the middle, we make raw_int divided by 2 minus one to make life easier.

    def top(): #create a function that divides the image into top and bottom, and call it in the actual code.
        for counter in range(1, raw_int  + 2): #counter starts at one because we don't want 0 stars on the first row
            d = ""
            for x in range((raw_int + 1) - counter): #This creates the number of initial spaces. Uses function (x + 1) - Rows to get the right number of spaces in each row. Every time the larger for loop runs again, the inside one changes, allowing there to be a different number of spaces for each line.
                d = d + " "
            for y in range(2 * counter - 1): # fucntion 2x - 1, where x is the line number. Don't need to use how many total rows there are b/c it doesn't affect it.
                d = d + "*"
            print(d)

    def bottom():
        f = ""
        for counter in range(1, raw_int  + 1):
            for y in range(counter): #the space just repeats the number of times the row it is on.
                f = f + " "
            for x in range(fullraw_int + (-2 *counter)): #function -2x + rows, so each row is different.
                f = f + "*"
            print(f)
            f = ""
    top() #calls the functions above
    bottom()

#Calling the functions above
answer = int(input("Hello! Which challenge would you like to see? Pick between 1 and 4."))

if answer == 1:
    challenge_1()
elif answer == 2:
    challenge_2()
elif answer == 3:
    challenge_3()
elif answer == 4:
    challenge_4()
else:
    print("You didn't choose any of the choices... Try again?")












#
