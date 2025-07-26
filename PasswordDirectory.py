from tkinter import *
from PIL import ImageTk, Image

CREME = "#EBD4D0"
RED = "#AF3E3E"
FONT_NAME = "Segoe UI"


def savePwd():
    website = wtxt.get()
    email = etxt.get()
    password = ptxt.get()

    with open(file="Outputs/secrets.txt", mode="w") as f:
        f.write(f"{website}|{email}|{password}")


w = Tk()
w.title("Password Generator")
w.config(padx=20, pady=20, bg=CREME)
lbl = Label(text=" Password Generator ", font=(FONT_NAME, 20, "bold"), bg=CREME, fg=RED)
lbl.grid(column=1, row=0, columnspan=3)

canvas = Canvas(width=200, height=200, bg=CREME, highlightthickness=0)
original_image = Image.open("Resources/password.png")
resized_image = original_image.resize((180, 180), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=1, columnspan=3)

websiteLbl = Label(text=" Website: ", font=(FONT_NAME, 10, "bold"), bg=CREME, fg=RED)
websiteLbl.grid(column=1, row=2)
wtxt = Entry(width=80)
wtxt.grid(column=2, row=2, pady=20, columnspan=2)
wtxt.focus()


emailLbl = Label(text=" Email: ", font=(FONT_NAME, 10, "bold"), bg=CREME, fg=RED)
emailLbl.grid(column=1, row=3)
etxt = Entry(width=80)
etxt.grid(column=2, row=3, pady=20, columnspan=2)
etxt.insert(index=0, string="adity.kansara36@gmail.com")

pwdLbl = Label(text=" Password: ", font=(FONT_NAME, 10, "bold"), bg=CREME, fg=RED)
pwdLbl.grid(column=1, row=4)
ptxt = Entry(width=35)
ptxt.grid(column=2, row=4, pady=20)

pbtn = Button(text="generate Password", width=35)
pbtn.grid(column=3, row=4, pady=20)

btn = Button(text="Enter", width=50)
btn.grid(column=1, row=5, pady=20, columnspan=4)

w.mainloop()
