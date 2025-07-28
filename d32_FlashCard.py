from tkinter import *
from PIL import ImageTk, Image
import pandas as p
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Segoe UI"

frenchWords = p.read_csv("Resources/french_words.csv")
words = frenchWords.to_dict(orient="records")
af = None
currentcard = {}

#TODO : Remove from list code

def turnCard():
    global currentcard
    canvas.itemconfig(img, image=backphoto)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(txt, text=currentcard["English"])


def rightBtn():
    global af, currentcard
    w.after_cancel(af)
    currentcard = random.choice(words)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(txt, text=currentcard["French"])
    canvas.itemconfig(img, image=photo)
    af = w.after(3000, turnCard)


w = Tk()
w.title("Flashy")
w.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

af = w.after(3000, turnCard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
original_image = Image.open("Resources/card_front.png")
photo = ImageTk.PhotoImage(original_image)
backphoto = ImageTk.PhotoImage(file="Resources/card_back.png")
img = canvas.create_image(400, 263, image=photo)
title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
txt = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

wr = ImageTk.PhotoImage(file="Resources/wrong.png")
wrongBtn = Button(image=wr, highlightthickness=0, bg=BACKGROUND_COLOR)
wrongBtn.grid(row=1, column=0)

rt = ImageTk.PhotoImage(file="Resources/right.png")
wrongBtn = Button(image=rt, highlightthickness=0, bg=BACKGROUND_COLOR, command=rightBtn)
wrongBtn.grid(row=1, column=1)

rightBtn()

w.mainloop()
