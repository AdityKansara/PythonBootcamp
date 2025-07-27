from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Resources.data import letters, nums, special
from beginnerPackage import pyperclip
import json

CREME = "#EBD4D0"
RED = "#AF3E3E"
FONT_NAME = "Segoe UI"
SECRETS_PATH = "Outputs/secrets.json"


def searchPwd():
    website = wtxt.get()
    if website:
        try:
            with open(file=SECRETS_PATH, mode="r") as f:
                secrets = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(
                title=" Password Generator ",
                message=f"Credential File does not exist",
            )
            return

        if website in secrets:
            messagebox.showinfo(
                title=" Password Generator ",
                message=f"Your credentials for {website} is..\n email = {secrets[website]["email"]}\n password = {secrets[website]["password"]}",
            )
        else:
            messagebox.showinfo(
                title=" Password Generator ",
                message=f"Credentials for {website} does not exist.",
            )


def clear_fields():
    wtxt.delete(0, END)
    # etxt.delete(0, END)
    ptxt.delete(0, END)


def generatePwd():
    ptxt.delete(0, END)
    generated_password = []
    letter = [choice(letters) for _ in range(randint(4, 10))]
    num = [choice(nums) for _ in range(randint(2, 4))]
    sp = [choice(special) for _ in range(randint(2, 4))]
    generated_password = letter + num + sp
    shuffle(generated_password)
    final_pwd = "".join(generated_password)
    pyperclip.copy(final_pwd)
    ptxt.insert(index=0, string=final_pwd)


def savePwd():
    website = wtxt.get()
    email = etxt.get()
    password = ptxt.get()

    newSecrets = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website and email and password:
        ans = messagebox.askyesno(
            title=" Password Generator ",
            message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nAre these value correct?",
            default="yes",
        )
        if ans:
            try:
                with open(file=SECRETS_PATH, mode="r") as f:
                    secrets = json.load(f)
            except FileNotFoundError:
                secrets = {}
            secrets.update(newSecrets)
            with open(file=SECRETS_PATH, mode="w") as f:
                json.dump(secrets, f, indent=4)
                clear_fields()
            messagebox.showinfo("Success", "Credentials saved successfully!")

    else:
        messagebox.showerror(
            " Password Generator ", "Enter Every Field before proceeding!"
        )


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
wtxt = Entry(width=35)
wtxt.grid(column=2, row=2, pady=20)
wtxt.focus()
sbtn = Button(text="Search", width=35, command=searchPwd)
sbtn.grid(column=3, row=2, pady=20)

emailLbl = Label(text=" Email: ", font=(FONT_NAME, 10, "bold"), bg=CREME, fg=RED)
emailLbl.grid(column=1, row=3)
etxt = Entry(width=80)
etxt.grid(column=2, row=3, pady=20, columnspan=2)
etxt.insert(index=0, string="adity.kansara36@gmail.com")

pwdLbl = Label(text=" Password: ", font=(FONT_NAME, 10, "bold"), bg=CREME, fg=RED)
pwdLbl.grid(column=1, row=4)
ptxt = Entry(width=35)
ptxt.grid(column=2, row=4, pady=20)

pbtn = Button(text="generate Password", width=35, command=generatePwd)
pbtn.grid(column=3, row=4, pady=20)

btn = Button(text="Enter", width=50, command=savePwd)
btn.grid(column=1, row=5, pady=20, columnspan=4)

w.mainloop()
