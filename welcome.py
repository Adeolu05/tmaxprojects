a = "Adeniyi"
b = "Adeniyi62"
c = input ("Username: ")
d = input ("Password: ")

if a == c and b == d:
    print ("Welcome!",a)
elif a == c and b != d:
    print ("Invalid Password!")
else:
    print ("Access Denied!")
    
