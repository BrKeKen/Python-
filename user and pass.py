""" Take a input from the user for asking username and password. 
The user should be only allowed to keep the password if the username is valid. 
If both are valid print successful else unsucessful. """

username=input("Enter your username: ")
a=len(username)
if(a>4):
 password=input("Enter your password: ")
 print("username:",username)
 print("password:",password)
else:
 print("Invalid username")