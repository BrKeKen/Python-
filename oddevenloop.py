""" a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
for i in range(a,b):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd") """
""" 
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
a=0
b=0
for i in range(start, end + 1):
    if i % 2 == 0:
        a = a + 1
        print(f"{i} is Even")
    else:
        b = b + 1
        print(f"{i} is Odd")    
print("Total Even numbers: ",a)
print("Total Odd numbers:",b) """
""" 
a= int(input("Enter the length: "))
for i in range(a):
    c=int(input("Enter a number: "))
    if c % 2 == 0:
        print("Even")
    else:
        print("Odd") """
""" 
import time
a=int(input("Enter starting timer: "))
for i in range(a,0,-1): 
    print(i)
    time.sleep(1)
print("Time's up!") """

print("बाटोमा मेरो स्कुटरको टायर पन्चर भयो, त्यसैले म कक्षामा ढिलो पुगें।")
