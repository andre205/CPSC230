#Sum

x = int(input("How many numbers would you like to sum?"))

total = 0
v = 1

while v <= x:
    print("Enter number", str(v))
    n = int(input())
    v = v + 1
    total = total + n
    
print("The sum of those numbers is", total)
