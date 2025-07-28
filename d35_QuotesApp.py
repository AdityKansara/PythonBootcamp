import requests
from tkinter import *
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Segoe UI"


def getQuote():
    res = requests.get(url="https://api.kanye.rest", verify=False)
    res.raise_for_status()
    data = res.json()
    quote = data["quote"]

    canvas.itemconfig(title, text=quote)


w = Tk()
w.title("QuoteApp")
w.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=414, bg=BACKGROUND_COLOR, highlightthickness=0)
original_image = Image.open("Resources/chatBubble.png")
photo = ImageTk.PhotoImage(original_image)
img = canvas.create_image(150, 207, image=photo)
title = canvas.create_text(
    150, 207, text="hello", width=200, font=(FONT_NAME, 20, "italic")
)
canvas.grid(column=0, row=0)

rt = ImageTk.PhotoImage(file="Resources/manEmoji.png")
wrongBtn = Button(image=rt, highlightthickness=0, bg=BACKGROUND_COLOR, command=getQuote)
wrongBtn.grid(row=1, column=0)

w.mainloop()
