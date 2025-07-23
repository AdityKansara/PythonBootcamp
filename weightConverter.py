from tkinter import *

w = Tk()
w.title("Weight Converter")
w.minsize(300, 300)
a = 0

txt = Entry(width=10)
txt.grid(column=2, row=0, padx=100, pady=20)
lbl = Label()
lbl.config(text="Enter your weight in KG")
lbl.grid(column=2, row=2, pady=20)


def btnClick():
    a = txt.get()
    a = round(float(a) * 2.205, 2)
    lbl.config(text="Weight in lbs is " + str(a))


btn = Button(text="Convert", command=btnClick)
btn.grid(column=2, row=1, pady=20)

w.mainloop()
