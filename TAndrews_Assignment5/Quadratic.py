#Quadratic Formula with whiles

import math

a=float(input("What is a?"))
b=float(input("What is b?"))
c=float(input("What is c?"))

while ((b**2)-4*a*c) < 0:
    print("Those values produce a negative desciminate. Please reentter the values.")
    a=float(input("What is a?"))
    b=float(input("What is b?"))
    c=float(input("What is c?"))


sol1=((-b)+ (math.sqrt((b**2)-4*a*c))) /(2*a)
sol2=((-b)- (math.sqrt((b**2)-4*a*c))) /(2*a)
print("The roots of the function are",sol1,"and",sol2)
