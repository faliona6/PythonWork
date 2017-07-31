#Story Time with Fiona!

#stage 1
answer_1 = input("Today is a beautiful day. The sun is shining, birds are singing, the flowers are blooming. You take a seat outside on the patio and decide that you want a little snack. do you want to each CAKE or PIE?")

if answer_1 == "CAKE":
    answer_2 = input("You chose to eat cake. The cake was very tasty but your stomach started to feel very uncomfortable. You are feeling unwell." +
    "Do you want to REST or take a SHOWER?")
elif answer_1 == "PIE":
    answer_3 = input("You chose to eat the pie. It was okay, but you started to see some funny things. There was an elf next to you. Do you choose"
    + "to FIGHT the elf or LEAVE IT ALONE?")
else:
    print("You chose to eat nothing. Case sensitive. Try again.")
# stage 2 CAKE

if answer_2 == "REST":
    answer_4 = input("You chose to take a rest in the bed. However, when you woke up, you realized that you are in a magical land! There were" +
    "unicorns everywhere, rainbows even more everywhere, and lots of cotton candy. The land is very vast and looks like it goes on" +
    "forever. The bed is still there. Will you go EXPLORE or STAY at the bed?")

elif answer_2 == "SHOWER":
    print("You bonked your head on the shower because you were feeling unwell. You died from blood loss. Sorry. Try again.")

else:
    print("You died from doing nothing. Try again.")

#stage 2 PIE
if answer_3 == "FIGHT":
    answer_5 = input("You chose to fight the magical elf! However, you are a mere human and therefore cannot beat such a magical and " +
    "higher up being! You lost with a terrible defeat and died. Try again.")
elif answer_3 == "LEAVE IT ALONE":
    print("You chose to do nothing. However, the elf is angry because that's its personality. It hit you in the head and you died. Try again.")
