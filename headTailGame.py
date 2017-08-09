from random import randint

ScoreDoc = open("scores.txt", "r")
key = ScoreDoc.readline()

highScore = {
}
ScoreDoc.close()

with open("scores.txt") as table:
    for line in table:
        (key, val) = line.split()
        highScore[key] = int(val)


username = input("What's your username?")
highScore[username] = 0
start = 0
while start == 0:

    user = input("Heads or Tails? 'H' or 'T'   ")
    coin = randint(0,1)

    if coin == 0:
        print("The coin says Tails.")
        if user == "H":
            print("You lose!")
            start = 1
        if user == "T":
            print("You win!")
            highScore[username] = highScore[username] + 1
    if coin == 1:
        print("The coin says Heads.")
        if user == "H":
            print("You win!")
            highScore[username] = highScore[username] + 1
        if user == "T":
            print("You lose!")
            start = 1

for let, count in highScore.items():
    a = ("Username: " + let + "\tScore: " + str(count))
    print(a)

ScoreDoc = open("scores.txt", "w")


for key, value in highScore.items():
    ScoreDoc.write(key + " " + str(value) + "\n")
