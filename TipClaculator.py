# TipCalculator
print("Welcome to tip Calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip / 100)
split = total_bill / people

print(f"Each person should pay ${round(split,2)}")
