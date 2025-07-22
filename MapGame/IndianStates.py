import turtle
import pandas as p

TOTAL_STATES = 36

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


def createName(state, x, y):
    name = turtle.Turtle()
    name.color("black")
    name.hideturtle()
    name.penup()
    name.goto(x, y)
    name.write(state)


data = p.read_csv("IndianStates.csv")

s = turtle.Screen()
s.title("Indian States Game")
img = "IndiaMap.gif"
s.addshape(img)
turtle.shape(img)

allStates = False
stateNames = data["State/UT"].to_list()
correctAns = []
while not allStates:
    answer = s.textinput(
        f"{len(correctAns)}/{TOTAL_STATES} States", "Tell me the name of the state:"
    ).title()
    if answer == "Exit":
        break
    if answer in stateNames:
        if answer not in correctAns:
            correctAns.append(answer)
        stateDetails = data[data["State/UT"] == answer]
        x = stateDetails.X.item()
        y = stateDetails.Y.item()
        n = stateDetails["State/UT"].item()
        createName(n, x, y)

    if len(correctAns) == 36:
        allStates = True

remaining = []
for ans in stateNames:
    if ans in correctAns:
        continue
    else:
        remaining.append(ans)
newData = p.DataFrame(remaining)
newData.to_csv("RemainingStates.csv")
s.exitonclick()
