from tkinter import *
root = Tk()

Player = []
y = {}
z = 0

a = Label(root, text= "Number of Players").pack()
b = Entry(root)
b.pack()

Player = int (b.get())

def start(event):
    while Player != 0:
        d = Label(root, text= "Player Name").pack()
        e = Entry(root)
        e.pack()
        f = e.get()

        def add():
            Player.append(f)
            c -= 1
            e.delete(0, END)

        g = Button (root, text= "ADD USER", command = add)

d = Button(root, text="START", command = start).pack


root.mainloop()