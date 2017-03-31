#Quadratic Formula

import math

ai=input("What is a?")
bi=input("What is b?")
ci=input("What is c?")
a=float(ai)
b=float(bi)
c=float(ci)

sol1=((-b)+ (math.sqrt((b**2)-4*a*c))) /(2*a)
sol2=((-b)- (math.sqrt((b**2)-4*a*c))) /(2*a)

print("The roots of the function are",sol1,"and",sol2)
