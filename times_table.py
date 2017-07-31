#Times table

rows = input("How many rows/columns do you want?")
rows_int = int(rows)

def func(a): #Defining functions
    wholeString = ""
    for column in range(1, rows_int + 1): #Loop so that every column adds a string which is the column number times the row nubmer.
        wholeString = wholeString + str(a * column) + "\t"
    return wholeString

for counter in range(1, rows_int + 1):
    entireString = func(counter) #Within this for loop, exetute function func.
    print(entireString) # once wholeString is returned, print entireString.
    wholeString = "" #Reset wholeString to an empty string






























#a = ""
#for x in range(rows_int):
    #print ("")
    #a = ""
    #for y in range(rows_int):
        #print(a + str(y))
        #a = a + str(y)
