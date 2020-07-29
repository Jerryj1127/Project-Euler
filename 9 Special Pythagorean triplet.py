from math import sqrt
a,b,c = 0,0,0

for a in range(999):
    for b in range(999):
        c = sqrt(a**2 + b**2)
        if a+b+c == 1000:
            print(a*b*c)