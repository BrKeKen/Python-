""" Take a input from the user for asking username and password. 
The user should be only allowed to keep the password if the username is valid. 
If both are valid print successful else unsucessful. """

user=input("Enter your username: ")
a=len(user)
if(a>4):
 password=input("Enter your password: ")
 print("user:",user)
 print("password:",password)
else:
 print("Invalid username")