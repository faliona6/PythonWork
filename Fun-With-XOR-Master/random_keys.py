import random

students = ["Salina", "Fiona", "Lucia", "Jasmine", "Jenna", "Nadine", "Sonja",
"Soliana", "Liz", "Rita", "Molly", "Kathryn", "Yujing", "Abigail", "Katie",
"Isha", "Shriya", "Gabi", "Lisa", "Megan"]

def random_key(n):
    key = ""
    for i in range(n):
        key += str(random.randint(0,1))
    return key

# Fill in table with random keys (triangular array)
f = open("random_keys.txt", "w")
for i in range(len(students)):
    for j in range(i):
        f.write(students[i] + " " + students[j] + " " + random_key(140*7) +"\n")

f.close()
