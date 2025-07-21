names = []
with open("./Friends.txt", "r") as nameFile:
    name = nameFile.read()
    names = name.splitlines()

with open("./Letter.txt", "r") as letterFile:
    lines = letterFile.readlines()

    for eachName in names:
            linesplit = lines[0].split(" ")
            linesplit[1] = f"{eachName}!"
            newLine = " ".join(linesplit)+ "\n"
            newLetterLines = [newLine] + lines[1:]
            with open(f"{eachName}.txt", "w") as tmpFile:
                tmpFile.writelines(newLetterLines)
