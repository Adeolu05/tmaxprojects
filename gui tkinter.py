from tkinter import *

root = Tk()
a = Label (root, text = "STUDENT LOGIN PORTAL", bg="White", fg="Black").grid(row=1, column=1)
b = Label (root, text = "Student ID", bg = "Red", fg = "White").grid(row=2, column=1)
c = Entry (root, text = "Student ID").grid(row=2, column=2)
d = Label (root, text = "Student Password", bg = "REd", fg = "White").grid(row=3, column=1)
e = Entry (root, text = "Student Password").grid(row=3, column=2)
f = Button (root, text = "Submit").grid(row=5, column=1)
g = Label (root, text = "forgot password?", bg="White", fg="Black").grid(row=4,column=1)

root.mainloop()
