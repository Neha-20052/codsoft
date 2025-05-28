
print("simple calculator")

a = int(input("Enter the value of a= "))
b = int(input("Enter the value of b= "))

choice = input("Enter the '+','-','*','/','%'=  ")

if (choice =='+'):
    result = a + b
    print("result", result)

elif (choice == '-'): 
    result = a - b
    print("result" , result)

elif (choice == '/'):
    result = a / b
    print("result", result)

elif (choice == '*'): 
    result = a * b
    print("result", result)

elif (choice == '%'):
    result = a % b
    print("result", result)
    
else :
    print("No operation are match")




    