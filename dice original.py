'''import random

min_val=1
max_val=6
min_val=1
max_val=6

print ("DICE GAME")
Player= int(input("Numbers of Players?: "))
a = []

while Player >=1:
    if Player==1:
        b = input("Player Name: ")
        a.append (b)
        print ("Welcome", a)
        roll_dice = (input("Roll dice? "))
        while roll_dice == 'yes' or roll_dice == 'y':
            print ("Rolling dice... ")
            print ("The values are: ")'''



'''import random

min = 1
max = 6

name = []
print ("THE DICE GAME\n")
player = int(input("Numbers of players? "))

while player >=1:
    a = input("Enter the player Names: ")
    name.append(a)
    player -=1

b = player

for c in name:
    d = input("Press p to roll the dice ")
    print (name[b], random.randint(1,6), ':', random.randint(1,6))
    b +=1'''




import random

a = int(input("Enter the number of Players: "))
Player = []

y = {}
z = 0

while a != 0:
    b = input ("Player Name: ")
    Player.append(b)
    a -= 1

for x in Player:
    c = int(input("\nPress 1 to roll dice: "))
    
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = a + b

    y  [Player[z]] = c
    print(Player[z], ': ', a, ':', b)
    
    z += 1

print('\n', y)