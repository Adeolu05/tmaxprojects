from tkinter import *

root = Tk()
root.title ("Movie Ticket Booking Pg1")
root.config (bg= "Black")

def exi():
    global root
    root.destroy()

def more():
    m = Label (root, text= "↪coming soon......", fg= "White", bg= "Grey").grid(row=5, column=1)

def Next():
    new = Tk()
    new.geometry ("800x500")
    new.title ("Movie Ticket Booking Pg2")
    def sub():
        g= Label (new, text="Choose your time:", font=("Cambria", 16)).grid (row=18, column=0)
    def Next3():
        f= Label (new, text="How many ticket do you want to book?: ", font=("Cambria", 16)).grid (row=14, column=0)
        f1= Entry (new)
        f1.grid (row=14, column=1)
        f2= Button (new, text="Submit", width=10, command= sub).grid (row=14, column=2)
    def Next2():
        d= Label (new, text="Which movie do you want to watch?", font=("Cambria Bold", 16)).grid (row=7, column=0)
        d1= Checkbutton (new, text="Black Panther: Wakanda Forever", font=("Cambria", 14)).grid (row=8, sticky=W)
        d2= Checkbutton (new, text="Black Adam", font=("Cambria", 14)).grid (row=9, sticky=W)
        d3= Checkbutton (new, text="The Woman King", font=("Cambria", 14)).grid (row=10, sticky=W)
        e= Button (new, text= "Next", width=20, command= Next3).grid (row=11, column=0)
    
    a= Label (new, text="Where do you want to watch the movie?", font=("Cambria Bold", 16)).grid (row=1, column=0)
    b= Checkbutton (new, text="Abeokuta", font=("Cambria", 14)).grid (row=2, sticky=W)
    b1= Checkbutton (new, text="Abuja", font=("Cambria", 14)).grid (row=3, sticky=W)
    b2= Checkbutton (new, text="Ikeja", font=("Cambria", 14)).grid (row=4, sticky=W)
    c= Button (new, text= "Next", width=20, command= Next2).grid (row=5, column=0)

    
    new.mainloop ()
    

a = Label (root, text = "₰IZ99✓", font=("Cambria Bold", 20), fg="White", bg="Black").grid (row=0, column= 1)
a0= Label (root, text= "Movie ticket ®", font=("Cambria"), fg="White", bg="Black").grid (row=1, column=1)
a1= Button (root, text= "⌂ Menu", font=("Cambria", 12), width=20, height=1, bg= "Black", fg= "White").grid (row=2, column=1, padx=20, pady=20)
a2= Button (root, text = "Book a ticket", font=("Cambria", 14),fg="White", bg="Dark Green", width=25, command= Next).grid (row=4, column=0)
a3= Button (root, text= "Click for more", font=("Cambria", 14),fg="White", bg="Dark Blue", width=25, command= more).grid (row=4,column=1)
a4= Button (root, text= "Exit", font=("Cambria", 14),fg="White", bg="Red", width=25, command= exi).grid (row=4,column=2)





root.mainloop()
