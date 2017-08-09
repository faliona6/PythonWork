
word = input("What is the magical word?")

def Dictionary(word):
    dictionary = {}
    a = 0
    for letter in word:
        if letter in dictionary:
            dictionary[letter] = dictionary[letter] + 1
        else:
            dictionary[letter] = 1
    return dictionary

dictionary = Dictionary(word)
for let, count in dictionary.items():
    print("Letter: " + let + "\tCount: " + str(count))
