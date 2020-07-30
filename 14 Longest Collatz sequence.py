import time
start_time = time.time()

current_ittr = 1
big = 0

while(current_ittr<1000000):
    num = current_ittr
    count = 1
    while(num != 1):
        if num%2==0:
            num = num/2
        else:
            num = (num*3)+1
        count +=1
    if count>big:
        big = count
        data = current_ittr
    current_ittr += 1

print('\n\tRequired no: ', data, 'length: ',big)
print("--- %s seconds ---" % (time.time() - start_time))