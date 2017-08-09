wordBank = {"hello", "telephone", "killme", "sometimesicry", "yeboiiiii"}
actualWord = set()
playerSet = set()
chosenWord = wordBank.pop() #get the word from word bank, random
wordGuess = list(chosenWord)

actGuess = []

for letter in chosenWord:
    actualWord.add(letter) #turn letters in chosen Word into sets

x = len(chosenWord)
print("The chosen word is " + str(x) + " long.")

for letter in range (x): #Initial ___'s
    actGuess.append("_")


i = 9
while i > 0: #i is number of tries, decreases when u get something wrong
    a = ""
    if ("_" in actGuess): #While there are empty _'s, keep asking for letters
        print("You have " + str(i) + " more tries~")
        for y in actGuess: #prints the guessing word
            a = a + y
        print(a)
        print(" ")
        print("You have guessed: ") #prints everything you've guessed
        print(playerSet)
        user = input("What letter will you guess? \t")
        chosenWord.count(chosenWord)
        if (user in actualWord): #if it's in the actual word, remove letter from set
            actualWord.remove(user)
            print("--------------------------")
            print("You got a letter!")
            for count in range(x): #everytime you find the letter in the actual word, replace it
                if wordGuess[count] == user:
                    actGuess[count] = user
        elif(user in playerSet):
            print("--------------------------")
            print("Uh, you already guessed that. Are you blind?")
            i = i - 1 #counter down 1
        else:
            print("--------------------------")
            print("Sorry, that's not right.")
            i = i - 1 #counter down 1
        playerSet.add(user) #adds to list of what you've guessed
    else:
        break
if ("_" in actGuess):
    print("You lost! Sorry, too bad, sux for u.")
else:
    print("Congrats! You got the word~~~")
    print("It's " + chosenWord + "!")
