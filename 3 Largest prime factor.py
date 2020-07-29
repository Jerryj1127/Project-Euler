'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

#code
from math import sqrt
limit =  600851475143

def check_prime(num):
    for j in range(int(sqrt(num)), 1, -1):
        if num%j == 0:
            flag = False
            for i in range(int(sqrt(j)), 1, -1):
                if j%i == 0:
                    flag = True
            if flag != True:
                print(j)
                break

check_prime(limit)
print('done')


"""def prime(x):
    i=2
    while i<=x/i:
        
        if x%i==0:
            print(x)
            x=x/i
        else:
            i+=1
"""