'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

#code
num1,num2,num3,sum = 0,1,1,0
limit = 4000000

def check_even(num):
    if num%2 == 0:
        return num
    return 0

while(num3 < limit):
    sum += check_even(num3)
    num1 = num2
    num2 = num3
    num3 = num1+num2

print(sum)