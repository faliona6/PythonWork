import sys

student1 = sys.argv[1].lower()
student2 = sys.argv[2].lower()

# Look for your key in the file
found_it = False
f = open("random_keys.txt", "r")
for line in f:
    arr = line.split()
    st1 = arr[0].lower()
    st2 = arr[1].lower()
    key = arr[2]
    if st1 == student1 and st2 == student2 or st1 == student2 and st2 == student1:
        print(key)
        found_it = True
        break
if not found_it:
    print("Error: Could not find key :'(")
f.close()
