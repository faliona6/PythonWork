#Recipe Book
mon = open("money.txt", "r")
read = mon.readline()
money = int(read)
start = 1
RecipeBook = {
    "Cake" : {
        "Ingredients" : {
            "Flour" : 1,
            "Cheese" : 2
        }
    },
    "Pie" : {
        "Ingredients" : {
            "Dough" : 1,
            "Flour" : 1,
            "Rasberries" : 2
        }
    },
    "Crepe" : {
        "Ingredients" : {
            "Dough" : 1,
            "Flour" : 3,
            "Cheese" : 2
        }
    }
}
shop = {
    "Flour" : 500,
    "Cheese" : 300,
    "Dough" : 500,
    "Rasberries" : 600
}

sell = {
    "Flour" : 100,
    "Cheese" : 3,
    "Dough" : 100,
    "Rasberries" : 100,
    "Cake" : 900,
    "Pie" : 1000
}
pantry = {
"Flour" : 1
}
with open("pantry.txt") as table:
    for line in table:
        (key, val) = line.split()
        pantry[key] = int(val)

while start == 1:
    print("~~~~START~~~~")
    print("Money = " + str(money))
    print("Welcome to the 'Cooking Life' Game.")
    print(" ")
    print("Press 'i' for inventory")
    print("Press 's' for shop")
    print("Press 'r' for recipies")
    print("Press 'x' to sell")
    print("Press 'y' to save")
    print("Press 'q' for quit")
    user = input("What do you want to do?")
    #Inventory
    if user == "i":
        print("~~~~PANTRY~~~~")
        for count in pantry:
            print("Ingredient: " + str(count) + "\tQuantity: " + str(pantry[count]))
    #Shopping
    if user == "s":
        print("~~~STORE~~~")
        print("Money = " + str(money))
        for count in shop:
            print("Ingredient: " + str(count) + "\tPrice: " + str(shop[count]))
        buy = input("What do you want to get? Press 'q' to quit.")
        number = int(input("How many do you want?"))
        if shop[count] * number > money:
            print("You don't have enough money to buy this.")
        else:
            if buy in pantry:
                pass
            else:
                pantry[buy] = 0
            pantry[buy] = pantry[buy] + number
            money = money - shop[count] * number
            print("Money = " + str(money))
    #Recipies
    if user == "r":
        print("~~~~RECIPIES~~~~")
        #printing out recipies into CP
        for pastry in RecipeBook:
            print(pastry)
            for title in RecipeBook[pastry]:
                print (title)
                for ingredient in RecipeBook[pastry][title]:
                    print(ingredient + "\tQuantity: " + str(RecipeBook[pastry][title][ingredient]))
            print("----------------------------")

        #This is what you have:
        print("Your Inventory: ")
        for count in pantry:
            print("Ingredient: " + str(count) + "\tQuantity: " + str(pantry[count]))

        #Making something
        user = input("What would you like to make?")
        quantity = int(input("How many would you want?"))
        #Deleting the stuff in inventory
        hello = 0
        while hello == 0:
            for count in RecipeBook[user]["Ingredients"]:
                print(count in pantry)
                print(count)
                if (count in pantry):
                    if (pantry[count] < RecipeBook[user]["Ingredients"][count] * quantity):
                        print("You are short " + str((RecipeBook[user]["Ingredients"][count] * quantity) - pantry[count]) + " "+ count)
                        hello = 1
                    else:
                        pass
                else:
                    print("You are missing " + str(RecipeBook[user]["Ingredients"][count] * quantity) + " " + count)
                    hello = 1
            hello = 2
        if hello == 2:
            for count in RecipeBook[user]["Ingredients"]:
                print("hehehehhe")
                pantry[count] = pantry[count] - (RecipeBook[user]["Ingredients"][count] * quantity)
                if pantry[count] == 0:
                    del pantry[count]
                pantry[user] = quantity

    if user == "x":
        print(money)
        print("~~~SELL STUFF?~~~")
        for count in sell:
            print("Ingredient: " + str(count) + "\tSell For: " + str(sell[count]))
        print("Your inventory:")
        for count in pantry:
            print("Ingredient: " + str(count) + "\tQuantity: " + str(pantry[count]))
        whatSell = input("What do you want to sell?")
        number = int(input("How many would you like to sell?"))
        if pantry[whatSell] < number: #If you don't have enough of ingredient
            print("Sorry, can't sell what you don't have")
        else:
            money = money + (sell[whatSell] * number)
            for pastry in range(number): #removes the struff from pantry
                pantry[whatSell] = pantry[whatSell] - 1
                if pantry[whatSell] == 0: #Deletes the item if it has 0
                    del pantry[whatSell]
    #quit
    if user == "q":
        print("Bye!")
        start = 0
    #save
    PantryDoc = open("pantry.txt", "w")
    PantryDoc.close()
    if user == "y":
        PantryDoc = open("pantry.txt", "w")
        print("Saved!")
        for key, value in pantry.items():
            PantryDoc.write(key + " " + str(value) + "\n")
        PantryDoc.close()
        monn = open("money.txt", "w")
        monn.write(str(money))
        monn.close()















#
