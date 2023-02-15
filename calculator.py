def addition():
    print ("Addition(+)")
    a = float(input("Enter a number: "))
    b = 0
    ans = 0

    while a!=0:
        ans = ans+a
        b += 1

        a  = float(input("Enter another number (0 to calculate): "))
        return[ans,b]

def subtraction():
    print ("Subtraction(-)")
    a = float(input("Enter a number: "))
    b = 0
    sum = 0
    
    while a!=0:
        ans = ans-a
        b += 1

        a = float(input("Enter another number (0 to calculate): "))
        return [ans,b]

def multiplication():
    print ("Multiplicaton(*)")
    a = float(input("Enter a number: "))
    b = 0
    ans = 1

    while a!=0:
        ans = ans*a
        b += 1

        a = float(input("Enter another number (0 to calculate): "))
        return [ans,b]

def division():
    print ("Division(/)")
    an = []
    an = addition()
    a = an[1]
    b = an[0]
    ans = b/a

    return [ans,a]


while True:
    list = []
    print ("OPERATOR PROGRAM")

    print ("Enter '+' for addition")
    print ("Enter '-' for subtraction")
    print ("Enter '*' for multiplication")
    print ("Enter '/' for division")
    print ("Enter 'q' to quit")

    c = input(" ")
    if c != 'q':
        if c == '+':
            list = addition()
            print ("Ans = ", list[0], "total inputs", list[1])

    elif c == '-':
        list = subtraction()
        print ("Ans = ", list[0], "total inputs", list[1])

    elif c == '*':
        list = multiplication()
        print ("Ans = ", list[0], "total inputs", list[1])

    elif c == '/':
        list = division()
        print ("Ans =", list[0], "total input", list[1])

    else:
        print ("Sorry, You entered an invalid character")