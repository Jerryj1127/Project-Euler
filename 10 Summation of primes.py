import time
start_time = time.time()

def prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
sum = 0
limit = 2000000
for i in range(2, limit+1):
    if prime(i):
        sum += i
print(sum)

print("\n--- %s seconds ---" % (time.time() - start_time))