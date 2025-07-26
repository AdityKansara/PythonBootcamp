import pandas as p

alpha = p.read_csv("Resources/NATO.csv")
nato = {row.Letter: row.Code for (index, row) in alpha.iterrows()}

userInput = input("Enter Your Name:").upper()
user = [nato[letter] for letter in userInput]
print(user)
