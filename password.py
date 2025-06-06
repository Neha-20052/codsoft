
import random
import string

#input the length 
length = int(input("enter the length of password: "))


digits = string.digits
symbol = string.punctuation
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

characters  = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

#generate password
password = ''
for i in range(length):
    password += random.choice(characters)

#generated password
print("Generated password: ", password)













    