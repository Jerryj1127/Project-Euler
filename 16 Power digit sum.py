import time
start_time = time.time()

value, sum = 2**1000, 0
for i in str(value):
    sum += int(i)
print('Sum of digits of 2**1000:', sum)

#          __OR__( Later i cam eup with a single line solution)

#print(sum([int(x) for x in str(2**1000)]))


print("\n--- %s seconds ---" % (time.time() - start_time))