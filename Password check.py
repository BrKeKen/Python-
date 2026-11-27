#Break condition
""" 
for i in range(1,6):
  username=input("Enter your username: ")
  password=input("Enter your password: ")
 
  if(username=="username" and password =="password"):
   print("Login successful")
   break
else:
  print("Try again later") """


for i in range(1,11):
    name = input("Enter your name: ")
    if name == "shiva":
        continue
    else:
        print("Hello",name)
        