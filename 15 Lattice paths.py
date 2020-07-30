import time
start_time = time.time()

def factorial(num):
    fact,i = 1,1
    while(i<=num):
        fact *= i
        i += 1
    return fact

p = 20
q = 20

paths = factorial(p+q) // (factorial(p) * factorial(q))
print("No of paths: ", paths)

print("--- %s seconds ---" % (time.time() - start_time))