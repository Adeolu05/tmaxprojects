"""import random

def again():
    a=random.randint (1,31)
    b= 1
    while b<=5:
        c = int (input ("Guess a number: "))
        if c == a:
            print ("You guessed right in", b, "trials")
            break
        elif c>30:
            print ("Guess between 1 and 30")
        elif c>a:
            print ("Your guess is high, guess lower ")
        elif c<a:
            print ("Your guess is low, guess higher")
    

        else:
            print ("Guess between 1 and 30")

        if b == 5 and c!= a:
            print ("\nOops no more attempts")
            

        b+=1 
        


again()
def playAgain():
    d = input('''
Do you want to play again?
press Y to play again
press N to quit
''').capitalize ()
    if d == 'Y':
        again()
        playAgain()
    elif d == 'N':
        print ("See you later")
    else:
        print ("Choose either Y or N")
        playAgain()
playAgain()"""


from tkinter import *
import random

root = Tk()
root.title ("Guessing Game")
root.geometry ("600x400")
root.configure(bg="Black")

e= random.randint(1,31)

def exi():
    root.destroy()
def submit():
    
    
    f= 1
    z= int(c.get())
    print (e)
    while f<=5:
        if z == e:
            g = Label (root, text= "Welldone. You guessed right ✓✓✓✓",bg= "Black", fg="White", font=("Cambria Bold", 12)).grid (row=4, column=1)
            
            h=  Button (root, text= "exit", command=exi, bg="Red", fg="White", font=("Arial Bold", 10)).grid (row=5, column= 1)
            
            break

        elif z>30:
            g= Label (root, text= "<<< ⇶ Guess between 1 and 30 >>>", bg="Black", fg="White", font=("Arial", 9)).grid (row=4, column=1)
            
        elif z<e:
            g= Label (root, text= "Your guess is lower ✕, guess higher ").grid (row=4, column=1)
            
        elif z>e:
            g= Label (root, text= "Your guess is higher ✕, guess lower").grid (row=4, column=1)
            
        else:
            g= Label (root, text= "Guess between 1 and 30......", bg="Black", fg="White").grid (row=5, column=1)

        f+=1
          
a = Label (root, text = "THE GUESSING GAME ⇄", font=("Cambria Bold", 20), bg="Black", fg="White").grid (row=0, column=1)
b = Label (root, text = "Guess a number: ", font=("Cambria", 16), bg="Black", fg="White").grid (row=1, column=0)
c = Entry (root, width=30)
c.grid (row=1, column=1)
d = Button (root, text = "Submit", font=("Cambria", 14), bg="Dark Green", fg= "White", command=submit ).grid (row=2, column=1)


root.mainloop()    
        


