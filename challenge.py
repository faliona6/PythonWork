#Random Number Challenge
import random

empty_list = []

def rand_counter():
    for count in range(100):
        the_list = [random.randint(10,99)] #the_list creates a random nubmer every time in it's own list
        empty_list.extend(the_list) #then the extend method adds the ranom value to the empty list
        #he_list = [] #this empties out the temporary list and th proccess starts over.
    print(empty_list) #After 100 times, it prints the completed list.

#Challenge 1, All numbers that are factors of 3
a = ""
print("The random list is:")
rand_counter()
print("")

for x in range(100):
    recieve = empty_list.pop() # going backwards in the list, we take every value in order and put it in recieve
    if recieve%3 == 0: # if that value/3 has no remainder, then add that value as a string to an empty string.
        a = a + str(recieve) + ", "
print("All of the numbers that are factors of 3 are: " + a) #print out empty string
print("")

#Challenge 2, All numbers that are factors of both 5 and 3

print("The next set of random numbers are:")
rand_counter()
b = ""
emp_list = []
for x in range(100):
    recieve = empty_list.pop() # going backwards in the list, we take every value in order and put it in recieve
    if recieve%3 == 0 and recieve%5 == 0: # if that value/3 has no remainder, then add that value as a string to an empty string.
        b = b + str(recieve) + ", "
        emp_list.append(recieve) #Also, if it meets the conditions, it will also add the int to the empty list emp_list.
print("All of the numbers that are both factors of 3 and 5 are: " + b)

x = sum(emp_list) #Add the sum of everything from emp_list, and print.
print("The sum of all these numbers are: " + str(x))
































        #
