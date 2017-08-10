class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class GroceryCart:
    def __init__(self):
        self.foods = {}
        self.cost = 0

    def makeNice(self):
        for food in self.foods:
            print("Food: " + food)
            for thing in self.foods[food]:
                print(str(thing) + ":  " + str(self.foods[food][thing]))
            print("")

    def total(self):
        return self.cost
    def addFood(self, Food, quantity):
        if (Food.name in self.foods) == True:
            self.foods[Food.name]["amount"] = self.foods[Food.name]["amount"] + quantity
            self.foods[Food.name]["price"] = self.foods[Food.name]["price"] + Food.price * quantity
        else:
            self.foods[Food.name] = {}
            self.foods[Food.name]["amount"] = quantity
            self.foods[Food.name]["price"] = Food.price * quantity
    def totalCost(self):
        for val in self.foods:
            self.cost = self.cost + self.foods[val]["price"] * self.foods[val]["amount"]
        return self.cost
    def removeFood(self, Food, quantity):
        if (Food.name in self.foods) == True:
            if self.foods[Food.name]["amount"] > quantity:
                self.foods[Food.name]["amount"] = self.foods[Food.name]["amount"] - quantity
                self.foods[Food.name]["price"] = self.foods[Food.name]["price"] - Food.price * quantity
                if self.foods[Food.name]["amount"] == 0:
                    del self.foods[Food.name]
            else:
                print("You don't have enough of this item :(")
        else:
            print("You don't have any of this item :(")



redCart = GroceryCart()
y = redCart.total()
apple = Food("apple", 200)
redCart.addFood(apple, 30)
banana = Food("banana", 500)
redCart.addFood(banana, 50)
cheese = Food("cheese", 500)
redCart.addFood(cheese, 50)

z = redCart.totalCost()
print("Total Cost: " + str(z))
print(redCart.foods)
print("")
redCart.removeFood(banana, 250)
print(redCart.foods)
print("")
redCart.makeNice()
