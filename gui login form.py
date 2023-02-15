from tkinter import *
root = Tk()
def Login():
    z=Tk()
    user=c.get()
    pas=e.get()
    if m==user and p==pas:
        h = Label(z, text="We're Glad you're here").pack()
    elif m==user and p!=pas:
        i = Label(z, text="Oops, the Password you entered wasn't Correct").pack()
    else:
        j = Label(z, text="So sorry, \'Access Denied\'").pack()
    z.mainloop()
         
m = "DAVID"
p = "dpa123"
a = Label (root, text="LOGIN FORM", bg="blue", fg="white").pack()
b = Label (root, text="UserID", bg="White", fg="Black").pack()
c = Entry (root, text="UserID")
c.pack()
d = Label (root, text="User Password", bg="White", fg="Black").pack()
e = Entry (root, text="User Password")
e.pack()
f = Button (root, text="Login", bg="Blue", fg="white", command=Login).pack()
root.mainloop()