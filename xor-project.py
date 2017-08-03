def xor(a,b):
    if (a == 1 and b == 0):
        return(1)
    elif (a == 0 and b ==1):
        return(1)
    elif (a == 1 and b == 1):
        return(0)
    elif (a == 0 and b == 0):
        return(0)
    else:
        print("something's not right")

def longString(list1, list2): #take 2 binary i guess strings, do the xor on them, and return 1 if they r the same and 0 if they are different
    a = ""
    for number in range(len(list1)):
        x = xor(int(list1[number]), int(list2[number]))
        a = a + str(x)
    return a

def letBin(letter): # Takes letter and converts to binary
    a = ""
    j = ord(letter)
    g = bin(j)
    g = g[2:]
    for number in range(8-len(g)):
        x = "0"
        a = a + x
    g = a + str(g)
    return g

def binLet(binary): # takes binary and converts to letter
    j = int(binary, 2)
    g = chr(j)
    return(g)

def wordBin(name): # turns WORDs into Binary
    l = ""
    for letter in name:
        g = letBin(letter)
        l = l + g
    return l

def binWord(binary): # turns binary into words again
    a = ""
    for count in range(0, len(binary), 8):
        prefix = binary[count:count + 8]
        y = binLet(prefix)
        a = a + y
    return a

def encryption(message, key):
    list1 = wordBin(message)
    w = longString(list1, key)
    return w

def decrypt(ciphertext, key):
    list1 = longString(ciphertext, key)
    h = binWord(list1)
    return h
def keyLength(key, name):
    if (len(key) < len(name) * 8):
        print("NOPE!!!!!!!")
    elif (len(key) > len(name) * 8):
        key = key[0:len(name) * 8]
        return key
    else:
        pass
doc = open("key.txt", "r")
doc1 =  open("message.txt", "r")
list1 = "10011010"
list2 = "01111001"
name = doc.readline()
key = doc.readline()

#x = longString() # calls function
#print(x)
'''
y = letBin("c") # converts letter to binary
print(y)
z = binLet(y) # converts binary back to letter
print(z)
w = wordBin(name)
print(w)
p = binWord(w)
print(p)
'''
key = keyLength(key, name)
print(key)
ask = input("Do you want to encrypt or or decrypt? Type 'e' for encrypt or 'd' for decrypt     ")
if (ask == "e"):
    r = encryption(name, key)
    print(r)
elif (ask == "d"):
    h = decrypt(r, key)
    print(h)
else:
    print("yeah no")
