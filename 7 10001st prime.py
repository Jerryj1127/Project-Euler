limit = 10001
count= 1
i = 1
def prime(num):
    for i in range(2, (num//2)+1):
        if num%i == 0:
            return False
    return True

while(count != limit+1):
    i+=1
    if prime(i):
        count +=1
print(i)