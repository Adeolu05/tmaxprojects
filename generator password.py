from random import sample
import string

print ("Welcome to Random Password Generator! ")
length = int(input("Enter Password Length: "))
chars = string.ascii_letters+string.digits+string.punctuation
password = "".join(sample(chars, k=length))
print ("Your generated Password is:", password)
