""" num1 ='8'
num2='9'
num3=int(num1)
num4=int(num2)
sum= num3+num4
print(sum) """


""" 
import math
a=9.87
print(math.trunc(a))
print(round(a)) """
""" 
a=[2,2,100,3,5,4,]
b=set(a)
c=sorted(b)
print(a)
print(b)
print(c) """

""" print(bool("False")) """

name=input("Enter your name")
try:
    num=int(name)
    print("Can be converted")
except:
    print("Cannot be converted")
