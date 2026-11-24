""" Design a traiffc light
where
if Red light then it should be stop
if Yellow then ready
if its Green go and if any other color then invalid
color should be entered by the user and can be any color
 """


color=input("Enter any color: ")
light= color.lower()
if(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Be Ready")
elif(light=="green"):
    print("Go")
else:
    print("Invalid color")
