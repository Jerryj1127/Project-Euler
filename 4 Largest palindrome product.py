right = 999
left = 999
big =0
data = ""

def palindrome(num):
    n = num
    a=0
    while(n>0):
        a *= 10
        a += n%10
        n = n//10
    return a==num

while(right>100):
    n = right*left
    if palindrome(n):
        if n>big:
            big = n
            data = "{}, {}".format(left, right)
    left -= 1
    if left == 100:
        left = 999
        right -= 1

print(big,"--->", data)
