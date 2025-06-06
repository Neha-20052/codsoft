contacts = {}

print("Contact Book")
print("1.create contact")
print("2.delete contact")
print("3.update contact")
print("4.view contact")
num = input("enter the number: ")
if num == '1':
   name = input("Enter the name : ")
   if name in contacts:
      print(f'contacts name{name} already exists')
   else:
      phone_number = input("Enter the phone_number: ")
      contacts[name] = {'phone_number':phone_number}
      print(f'contact name has been created successfuly')

elif num == '2':
   name = input("enter contact name to delete: ")
   if name in contacts:
      del contacts[name]
      print(f'contact name {name} has been deleted successfully ')
   else:
      print("contact not exist")

elif num =='3':
   name = input("enter name to update contact: ")
   if name in contacts:
      phone_number = input("enter updated phone_number:  ")
      contacts[ name] = {'phone_number':phone_number}
   else:
      print("contact not exist")

elif num == '4':
   name = input("enter your name to view: ")
   if name in contacts:
      contact = contacts[name]
      print(f'name : {name}')
   else:
      print("contact not exist")












