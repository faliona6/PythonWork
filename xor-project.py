import sys #python Filename.py -e/-d INPUT.txt KEY.txt OUTPUT.txt
# ^ imports system for command line arguments
def xor(a,b): # xor is a function for taking two integers if dif. return 1, else returen 0
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

def longString(list1, list2): #take 2 binary strings, turns them into single encrypted string
    a = ""
    for number in range(len(list1)):
        x = xor(int(list1[number]), int(list2[number]))
        a = a + str(x)
    return a

def letBin(letter): # Takes letter converts to ascii then converts it into binary
    a = ""
    j = ord(letter)
    g = bin(j)
    g = g[2:]
    for number in range(8-len(g)): #padding - adds the nubmer of 0's needed to make the entire string 8 digits long
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

def encryption(message, key): # takes message and encrypts it using key
    list1 = wordBin(message) # turns words into binary
    w = longString(list1, key) # xor function for two strings
    return w

def decrypt(ciphertext, key): # takes encrypted message and using key turns it into text again
    list1 = longString(ciphertext, key) # turns binary into ascii
    h = binWord(list1) # turns ascii into words
    return h
def keyLength(key, name): #makes length of key the same length of the message
    if (len(key) < len(name) * 8):
        print("NOPE!!!!!!!")
    elif (len(key) > len(name) * 8):
        key = key[0:len(name) * 8]
        return key
    else:
        pass
KeyText = open(sys.argv[3], "r") # takes command line argument, opens the file stated and reads it
NameText =  open(sys.argv[2], "r") # takes command line argument, opens message file
encryptDoc =  open(sys.argv[2], "r") # takes command line argument, reads encrypted file

'''list1 = "10011010" TEST CODE
list2 = "01111001"'''
name = NameText.readline() # name is the message.txt
name = name.rstrip("\n")
key = KeyText.readline() # key is key.txt
key = key.rstrip("\n")
encryptionDoc = encryptDoc.readline() # reads encrypted doument
encryptionDoc = encryptionDoc.rstrip("\n")

#x = longString() # calls function
#print(x)
'''
y = letBin("c") # converts letter to binary
print(y)
z = binLet(y) # converts binary back to letter TESTING
print(z)
w = wordBin(name)
print(w)
p = binWord(w)
print(p)
'''
key = keyLength(key, name) # Changes length of key

if (sys.argv[1] == "-e"): # if user wants to encrypt, do function encryption with file sys.argv[2] and key sys.argv[3].
    r = encryption(name, key)
    doc = open(sys.argv[4], "w") #open location of encryption output
    doc.write(r) #write encryption (r)
    doc.close()
    print(r) #print r in command prompt
elif (sys.argv[1] == "-d"):
    h = decrypt(encryptionDoc, key)
    doc = open(sys.argv[4], "w") #open location of decryption output
    doc.write(h) #writes decryption
    doc.close() #close
    print(h)
else:
    print("yeah no")
