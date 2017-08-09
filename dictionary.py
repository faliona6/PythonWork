dictionary = {
"hello" : {
    "Spanish": "hola",
    "Chinese": "ni hao",
    "Japanese": "konnichiwa"
},
"goodbye" : {
    "Spanish": "adios",
    "Chinese": "zai jian",
    "Japanese": "sayonara"
},
"heybuddy" : {
    "Spanish": "heyo",
    "Chinese": "heyeyeyey",
    "Japanese": "MUAHAHHA"
}
}
print("Here is the list of stuff that you can translate from English:")
for key in dictionary:
    print(key)

word = input("Which word do you want to translate?")
language = input("Which language do you want to translate into? Choose Random, Chinese, or Japanese")
print(dictionary[word][language])
