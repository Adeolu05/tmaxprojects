from tkinter import *
from datetime import date

root = Tk()
root.title("Age calculator")
root.geometry("700x300")
root.resizable(0,0)
root.config(bg="White")

def cal():
    today = date.today()
    e = a.get().capitalize()
    f = int (b.get())
    g = int (c.get())
    h = int (d.get())
    birthDate = date(f, g, h)
    age = today.year - birthDate.year
    if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
        age -= 1
    #age = today.year -f- ((today.month, today.day)<(g,h))
    #Label(root, text= (e, "You're ", age , "yrs old"), font=("Franklin Gothic Demi", 10), bg="White", fg="Black").grid (row=13, column=1)
    Label(root, text= f"Hayy {e}. You're {age} yrs old 👍", font=("Franklin Gothic Demi", 20), bg="White", fg="Black").grid (row=13, column=1)

Label (root, text="❏ Welcome to the Age Calculating Application", font=("Franklin Gothic Demi", 14), bg="White", fg="Green").grid(row=0, column=1)
Label (root, text="CALCULATE YOUR AGE ", font=("Franklin Gothic Demi", 10), bg="White", fg="Black").grid(row=1, column=1)
Label (root, text="What is your name? ➠", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid (row=3, column=0, padx=20)
a = Entry(root, bg="Grey",fg="White", font=12, width=20)
a.grid(row=3, column=1)
Label (root, text="PLEASE ENTER YOUR D.O.B", font=("Franklin Gothic Demi", 10), bg="White", fg="Black").grid(row=5, column=1)
Label(root, text="Year ➠ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid (row=6, column=0)
b = Entry(root, bg="Grey",fg="White", font=12, width=20)
b.grid (row=6, column=1)
Label (root, text="Month ➠ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid (row=7, column=0)
c = Entry(root, bg="Grey",fg="White", font=12, width=20)
c.grid(row=7, column=1)
Label(root, text="Day ➠ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid(row=8, column=0)
d = Entry (root, bg="Grey",fg="White", font=12, width=20)
d.grid (row=8, column=1)
Button(root, text="Calculate ✔", font=("Comic Sans MS", 10), bg="Green", fg="White", width= 12, command= cal).grid(row=10,column=1)
Button(root, text="Exit ❎", font=("Comic Sans MS", 10), background="Red", foreground="White",width=12, command=root.destroy).grid(row=15, column=1)

root.mainloop()