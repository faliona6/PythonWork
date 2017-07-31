import math
import random

#Name Generator
names = ["Fiona", "Valerie", "Nikakaka", "Cheeseball","Ohyeah"]
rand = random.randint(0,2)
print(names[rand])
print(" ")

#Menu Generator
appatizer = ["Calamari", "Cheeseball", "Mashed Potato", "French Fries"]
main_course = ["Udon", "Pizza", "Gyudon", "Ramen"]
dessert = ["Cheesecake", "Icecream", "Matcha Icecream"]

a = "For appatizers, I will have "
b = "For my main course, I will have "
c = "For dessert, I will have "

rando = random.randint(0,3)
rran = random.randint(0,2)
print(a + appatizer[rando])
print(b + main_course[rando])
print(c + dessert[rran])
print(" ")

#Haiku Generator
fiveSyllable = ["Today I went to the market", "I really love fish", "Yesterday was my death", "I really love cheese", "Anime gives life"]
sevenSyllable = ["Why do you do this to me", "You tried so hard but failed", "I thought that you were my friend", "You are sadder than my cat", "Take me out to the ball game"]

yoll = random.randint(0,4)
yell = random.randint(0,4)
print(fiveSyllable[yoll])
print(sevenSyllable[yoll])
print(fiveSyllable[yell])

print("")

for counter in range(5):
    print("-" + fiveSyllable[counter])

#List Challenge
import copy

#Challenge: make a list and see if a certain item on the list

#Method 1
"""def checkList(item, myList):
    variable = myList.count(item)
    if variable > 0:
        return True
    else:
        return False

sampleList = ["bushes", "flowers", "trees"]
sampleItem = "flowers"

hello = checkList(sampleItem, sampleList)
print(hello)
"""
sampleList = ["bushes", "flowers", "trees"]
sampleItem = "flowers"

#Method 2
"""
def checkList(item, myList):
    number = len(myList)
    for x in range(number):
        hello = myList.pop()
        if hello == item:
            return True
        else:
            pass
    return False

yolo = checkList("flowers", sampleList)
print(yolo)
print(sampleList)
"""
#Method 3

sampleList = ["bushes", "flowers", "trees"]
actualSampleList = copy.copy(sampleList)
"""
def checkList(item, myList):
    number = len(myList)
    for x in range(number):
        hello = myList.pop()
        if hello == item:
            return True
        else:
            pass
    return False # when something returns, it doesnt run the rest of the code
    sampleList = actualSampleList

yolo = checkList("flowers", sampleList)
sampleList = actualSampleList
print(yolo)
print(sampleList)
"""
#Method 4

def checkList(item, myList):
    length = len(myList)
    for count in range(length):
        if myList[count] == item:
            return True
        else:
            pass
    return False


yolo = checkList("flowers", sampleList)
print(yolo)



















#


























#
