import random
print ("You're welcome to THE DICE GAME")

a = int(input("Number of Players: "))
b = input("What is your name?: ")


min_val = 1
max_val = 6

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print ("Dices rolling...")
    print ("The values are :")
    print (random.randint(min_val,max_val))
    print (random.randint(min_val,max_val))
    roll_again = input("Roll the Dices Again?")
