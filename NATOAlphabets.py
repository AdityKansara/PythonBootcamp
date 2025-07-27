import pandas as p

alpha = p.read_csv("Resources/NATO.csv")
nato = {row.Letter: row.Code for (index, row) in alpha.iterrows()}
done = True
while done:
    userInput = input("Enter Your Name:").upper()
    try:
        user = [nato[letter] for letter in userInput]
        done = False
    except KeyError:
        print("Name should only have letters please!")
        done = True

print(user)
