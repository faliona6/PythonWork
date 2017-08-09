'''
To run this code:
key.py [Student1] [Student2] | xor.py [input-file] -[e|d] > [output-file]
'''

import sys

def binary(letter):
    bin_string =  bin(ord(letter))[2:] # chop off 0b at front
    # pad to 8 characters
    padding = 8 - len(bin_string)
    for i in range(padding):
        bin_string = "0" + bin_string
    return bin_string

def encrypt(message, key):
    b = ""
    count = 0
    for c in message:
        count += 1
        b += binary(c)
    length = len(b)
    short_key = key[:length]
    ctextbin = xor_str(b, short_key)
    return ctextbin

def decrypt(ciphertext, key):
    short_key = key[:len(ciphertext)]
    message_bin = xor_str(ciphertext, short_key)
    return binary_to_letters(message_bin)

def letter(binary):
    car = chr(int(binary,2))
    return chr(int(binary, 2))

def binary_to_letters(binary_str):
    # break it up into chunks of 8 and convert 8 at a time
    count = 0
    result = ""
    for i in range(0, len(binary_str), 8):
        count = count + 1
        chunk = binary_str[i:i+8]
        let = letter(chunk)
        result += let
    return result

def test_xor():
    for i in range(0,2):
        for j in range(0,2):
            print("The xor of " + str(i) + " and " + str(j) + " is " + str(xor(i,j)))

# Returns a xor b, where a and b are ints that are either 1 or 0
def xor(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 1
    elif a == 1 and b == 0:
        return 1
    elif a == 1 and b == 1:
        return 0
    else:
        return -1 # error

# Returns the xor of a and b, where a and b are binary strings
def xor_str(a, b):
    if len(a) != len(b):
        return -1 # error
    result = ""
    for i in range(len(a)):
        a_int = int(a[i])
        b_int = int(b[i])
        c_int = xor(a_int, b_int)
        result += str(c_int)
    return result

def program():
    input_filename = sys.argv[1]
    f = open(input_filename, "r")
    text = f.readline().rstrip("\n")
    key = input()
    whatdo = sys.argv[2]
    if whatdo == "-e":
        print(encrypt(text, key))
    elif whatdo == "-d":
        print(decrypt(text, key))
    else:
        print("Use cmd line options -e or -d")

program()
