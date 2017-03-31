#geometry.py

#area of circle
#circumference of a circle
#volume of a sphere
#volume of a cylinder

import math

def area(r):
    return math.pi * (r**2)

def circumference(r):
    return 2 * math.pi * r

def svolume(r):
    return (4/3) * math.pi * (r**3)

def cvolume(r,h):
    return math.pi * (r**2) * h


print(area(2))
print(circumference(3))
print(svolume(4))
print(cvolume(5, 6))

