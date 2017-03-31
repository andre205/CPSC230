import math
x=1
y = []
#Enter numbers until number entered is negative
while x >= 0:
    x = int(input("Enter an integer"))
    y.append(x)

y.sort()
print(y)

#mean

#sum of list y
total = 0
for i in range(len(y)):
    total += y[i]
#formula
m = total / len(y)
print("Mean:", m)

#st. dev
f=[]
for i in range(len(y)):
    t = (y[i] - m)**2
    f.append(t)

#sum of variances
totalf = 0
for i in range(len(f)):
    totalf += f[i]

#forumula
print("Standard deviation:", math.sqrt(totalf/len(f)))
