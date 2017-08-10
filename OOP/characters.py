class Character:
    def __init__(self, health, name):
        self.health = health
        self.name = name
    def __str__(self):
        healthInfo = " Health: " + str(self.health)
        nameInfo = "Name: " + self.name
        return nameInfo + healthInfo
    def changeName(self, newName):
        self.name = newName
    def eat(self, food):
        self.health = self.health + food
    def attack(self, player2):
        player2.health = player2.health - 10

char1 = Character(90, "Sammy")
char2 = Character(90, "Mr.Cat")
print(char1)
print(char2)
char1.eat(5)
print(char1)
char1.attack(char2)
print(char2)
