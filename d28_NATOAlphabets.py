import pandas as p

alpha = p.read_csv("Resources/NATO.csv")
nato = {row.Letter: row.Code for (index, row) in alpha.iterrows()}


def generateNato():
    userInput = input("Enter Your Name:").upper()
    try:
        user = [nato[letter] for letter in userInput]
        print(user)
    except KeyError:
        print("Name should only have letters please!")
        generateNato()


generateNato()
