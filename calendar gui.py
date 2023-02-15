from tkinter import *
import calendar
import random

root = Tk()

root.title("Calendar")
root.geometry("400x400")
root.config(bg="Black")
def View():
    m=Tk()
    e = c.get()
    cal = calendar.calendar(int(e), w=2, l=1)
    i = Label(root, text=cal, font="courier 12 bold", bg="white", fg="black", justify=LEFT)
    i.grid(row=4, column=2, padx=4, pady=10)
    m.mainloop()





a = Label(root, text="CALENDAR", font=("Cambria Bold", 20), bg="Black", fg="White").grid(row=0, column=0)
b = Label(root, text="Which year do you wish to view? ", font=("Cambria Bold", 15), bg="Black", fg="White").grid(row=1, column=0)
c = Entry(root)
c.grid(row=2, column=0)
d = Button(root, text="View",font=("Cambria Bold", 10), bg="Black", fg="White", command = View).grid(row=3, column=0)

root.mainloop()