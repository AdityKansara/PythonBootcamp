names = []
with open("Resources/Friends.txt", "r") as nameFile:
    name = nameFile.read()
    names = name.splitlines()

with open("Resources/Letter.txt", "r") as letterFile:
    lines = letterFile.read()

for eachName in names:
    personalized = lines.replace("[name]", eachName)

    with open(f"Outputs/{eachName}.txt", "w") as tmpFile:
        tmpFile.writelines(personalized)
