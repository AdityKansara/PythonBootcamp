import math
from tkinter import *
import winsound


RED = "#AF3E3E"
LIGHTRED = "#DC7474"
CREME = "#EBD4D0"
ORANGERED = "#FF4500"
FONT_NAME = "Segoe UI"
WORK_MINS = 1 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
reps = 0
streak = 0
timer = None


def resetTimer():
    global reps, streak, timer
    w.after_cancel(timer)
    streak = reps = 0
    startBtn.config(state=NORMAL)
    lbl.config(text="Pomodoro Timer")
    canvas.itemconfig(timer_text, text=f"00:00")


def startTimer():
    global reps
    startBtn.config(state=DISABLED)
    reps += 1
    if reps % 2 == 0:
        countDown(SHORT_BREAK)
        lbl.config(text="Short Break")
    elif reps % 8 == 0:
        countDown(LONG_BREAK)
        lbl.config(text="Long Break")
    else:
        global streak
        streak += 1
        countDown(WORK_MINS)
        lbl.config(text="Focus Timer")
        lbl2.config(text="🔥" * streak)


def countDown(count):
    min = math.floor(count / 60)
    sec = count % 60
    min = f"{min:02}"
    sec = f"{sec:02}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = w.after(1000, countDown, count - 1)
    else:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        startTimer()


w = Tk()
w.title("Pomodoro")
w.config(padx=10, pady=10, bg=CREME)
lbl = Label(text=" Pomodoro Timer", font=(FONT_NAME, 30, "bold"), bg=CREME, fg=RED)
lbl.grid(column=1, row=0)

canvas = Canvas(width=440, height=420, bg=CREME, highlightthickness=0)
tomatoImg = PhotoImage(file="Resources/pomodoro.png")
canvas.create_image(220, 210, image=tomatoImg)
timer_text = canvas.create_text(
    220, 250, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)
button_frame = Frame(bg=CREME)
button_frame.grid(column=1, row=3)

startBtn = Button(
    button_frame,
    text="Start",
    font=(FONT_NAME, 14, "bold"),
    fg="white",
    bg=RED,
    activebackground=LIGHTRED,
    relief="flat",
    padx=20,
    pady=5,
    command=startTimer,
)
startBtn.grid(column=0, row=3, padx=20)

resetBtn = Button(
    button_frame,
    text="Reset",
    font=(FONT_NAME, 14, "bold"),
    fg=RED,
    bg=CREME,
    activebackground=LIGHTRED,
    relief="ridge",
    padx=20,
    pady=5,
    command=resetTimer,
)
resetBtn.grid(column=1, row=3, padx=20)

lbl2 = Label(
    text="Streak", font=(FONT_NAME, 16, "bold"), bg=CREME, fg=ORANGERED, pady=10
)
lbl2.grid(column=1, row=2)

w.mainloop()
