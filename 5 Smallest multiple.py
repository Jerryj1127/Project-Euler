limit = 20
num = 1

def factors(n):
    lis = []
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return i
    return n

for i in range(1,limit+1):
        if num%i != 0:
            num *= factors(i)
print(num)
#232792560
