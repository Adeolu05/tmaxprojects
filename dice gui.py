from tkinter import *
import random
#import MessageBox

root= Tk()
root.title ("The Dice Game")
root.geometry ("600x400")
root.configure(bg="Black")

def submit():
    name = []
    player = int (c.get())
    if player == 1:
        def roll():
            namelist = f.get ()
            h = Label(root, text= namelist,font=("Arial",16)).grid(row=7, column=0)
            h1 = Label(root, text= random.randint(1,6), font=("Arial",16)).grid(row=7, column=1)
            h2 = Label(root, text= random.randint(1,6), font=("Arial",16)).grid (row=7, column=2)
            g = Label(root, text= "Computer:", font=("Arial",16)).grid(row=8, column=0)
            g1 = Label(root, text= random.randint(1,6), font=("Arial",16)).grid(row=8, column=1)
            g2 = Label(root, text= random.randint(1,6), font=("Arial",16)).grid (row=8, column=2)
    
        def sub2():
            g = Button (root, text="Roll dice", font=("Cambria", 16),  bg="Blue", fg="White", command= roll).grid(row=6, column=2)

        e = Label (root, text= "Enter the name of players: ", font=("Cambria", 16),  bg="Black", fg="White").grid (row=4, column=0)
        f = Entry (root)
        f.grid(row=4, column=1)
        g = Button (root, text= "submit", font=("Cambria", 14), bg="Dark Green", fg="White", command=sub2).grid(row=4, column=2)
    elif player == 2:
        def roll():
            namelist = f.get ()
            name_list2 = f1.get()
            h = Label(root, text= namelist,font=("Arial",16), bg="Black", fg="White").grid(row=7, column=0)
            h1 = Label(root, text= random.randint(1,6), font=("Arial",16), bg="Black", fg="White").grid(row=7, column=1)
            h2 = Label(root, text= random.randint(1,6), font=("Arial",16), bg="Black", fg="White").grid (row=7, column=2)
            g = Label(root, text= name_list2, font=("Arial",16), bg="Black", fg="White").grid(row=8, column=0)
            g1 = Label(root, text= random.randint(1,6), font=("Arial",16), bg="Black", fg="White").grid(row=8, column=1)
            g2 = Label(root, text= random.randint(1,6), font=("Arial",16), bg="Black", fg="White").grid (row=8, column=2)
            """if h1 and h2 > g1 and g2:
                m=Label(root, text="WIN").grid(row=10, column=1)
            else:
                m=Label(root, text="LOSE").grid(row=10, column=1)"""
    
        def sub2():
            g = Button (root, text="Roll dice", font=("Cambria", 16),  bg="Blue", fg="White", command= roll).grid(row=6, column=2)
        
        e = Label (root, text= "Enter the name of players: ", font=("Cambria", 16),  bg="Black", fg="White").grid (row=4, column=0)
        f = Entry (root)
        f.grid(row=4, column=1)
        f1 = Entry (root)
        f1.grid (row=5, column=1)
        g = Button (root, text= "submit", font=("Cambria", 14), bg="Dark Green", fg="White", command= sub2).grid(row=6, column=1)
    else:
        e = Label(root, text="One or Two players only", font=16,  bg="Black", fg="White").grid (row=4, column=1)

        
a = Label (root, text = "THE DICE GAME 🎲", font=("Cambria Bold", 20), bg="Black", fg="White").grid (row=0, column=1)
b = Label (root, text= "Number of players playing: ", font=("Cambria", 16),  bg="Black", fg="White").grid(row=1, column=0)
c = Entry (root)
c.grid(row=1, column=1)
d = Button (root, text="submit", font=("Cambria", 14), bg="Dark Green", fg="White", command= submit).grid (row=2, column=1)






root.mainloop()