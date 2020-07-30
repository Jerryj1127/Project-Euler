import time
start_time = time.time()

curr_no = 1
triangle = 0
count = 0

def factors(num):
    temp_count = 0
    for i in range(1, (int(num**0.5))+1):
        if num%i == 0:
            temp_count += 1
            if num//i != i:
                temp_count+=1
    #print(num, '---> ', temp_count-1)
    return temp_count-1

while(count<=500):
    triangle += curr_no
    curr_no += 1
    count = factors(triangle)
print(triangle)


print("--- %s seconds ---" % (time.time() - start_time))