from tkinter import *
from PIL import Image, ImageTk
import _mysql_connector as mysql
from tkinter.messagebox import showerror

root = Tk()
root.title ("LOGIN FORM")
root.config (bg= "Black")
         
m = "DAVID"
p = "dpa123"
a = Label (root, text="LOGIN FORM", font=("Cambria Bold", 20), fg="White", bg="Black").pack()
b = Label (root, text="UserID", font=("Cambria"), fg="White", bg="Black").pack()
c = Entry (root, text="UserID")
c.pack()
d = Label (root, text="User Password", font=("Cambria"),fg="White", bg="Black").pack()
e = Entry (root, text="User Password")
e.pack()
f = Button (root, text="Login", font=("Cambria", 14),fg="White", bg="Red").pack()
root.mainloop()
