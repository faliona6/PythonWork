doc = open("myName.txt", "w")
doc.write("hello there my friends\n")
doc.write("Fiona\n")
doc.write("Soetrisno\n")

doc = open("myName.txt", "r")
for line in doc:
    print(line.rstrip("\n"))
line = doc.readline()
line = line.rstrip("\n")
print(line)
doc.close()
