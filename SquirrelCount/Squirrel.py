import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

datadict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel],
}

df = pd.DataFrame(datadict)
df.to_csv("SquirrelCount.csv")
