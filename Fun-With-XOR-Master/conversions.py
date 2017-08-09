# Character to ASCII
# Example: 'a' --> 97
def c_to_a(c):
    return ord(c)

# ASCII to Character
# Example: 97 --> 'a'
def a_to_c(asc):
    return chr(asc)

# ASCII to Binary
# Example: 97 --> '01100001'
def a_to_b(a):
    binary = bin(a)[2:] # chop off leading two characters, which are '0b'
    # pad with leading 0's to reach 8 characters
    zeros_to_add = 8 - len(binary)
    for i in range(zeros_to_add):
        binary = "0" + binary
    # bin(a) returns 0b1100001
    # bin(a)[2:] returns 1100001
    # after padding, it is 01100001
    return binary

# Binary to ASCII
# Example: '01100001' --> 97
def b_to_a(b):
    return int(b, 2) # the 2 is for base 2, i.e. binary

def test_functions():
    c = "a"
    print("c: " + str(c))
    a = c_to_a(c)
    print("a: " + str(a))
    b = a_to_b(a)
    print("b: " + str(b))
    a = b_to_a(b)
    print("a: " + str(a))
    c = a_to_c(a)
    print("c: " + str(c))

test_functions()
