a = int(input("Enter a number of your choice: "))
b = int(input("Enter a number of your choice: "))

c = input ("Which operator do you want to use +, -, *, /,? ")

if c== '+':
   print (a, '+', b, '=', a+b)
elif c== '-':
     print (a, '-', b, '=', a-b)
elif c== '*':
     print (a, '*', b, '=', a*b)
elif c== '/':
     print (a, '/', b, '=', a/b)
else:
     ("You did not select any operator")
     
