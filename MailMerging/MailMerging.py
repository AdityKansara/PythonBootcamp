names = []
with open("./Friends.txt", "r") as nameFile:
    name = nameFile.read()
    names = name.splitlines()

with open("./Letter.txt", "r") as letterFile:
    lines = letterFile.read()

for eachName in names:
    personalized = lines.replace("[name]", eachName)

    with open(f"{eachName}.txt", "w") as tmpFile:
        tmpFile.writelines(personalized)
