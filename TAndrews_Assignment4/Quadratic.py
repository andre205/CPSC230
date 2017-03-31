#Quadratic Formula with ifs

import math

a=float(input("What is a?"))
b=float(input("What is b?"))
c=float(input("What is c?"))


if (b**2)-4*a*c > 0:
    sol1=((-b)+ (math.sqrt((b**2)-4*a*c))) /(2*a)
    sol2=((-b)- (math.sqrt((b**2)-4*a*c))) /(2*a)
    print("The roots of the function are",sol1,"and",sol2)
else: print("Error")
