#Prime number challenge

import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

theSum = []

thisList = [3, 6, 8, 4, 9, 10, 60, 17, 7]

for x in range (len(thisList)):
    number = thisList[x]
    if is_prime(number) == True:
        theSum.append(number)
        print(number)
    else:
        pass
total = sum(theSum)
print("the sum is: " + str(total))
