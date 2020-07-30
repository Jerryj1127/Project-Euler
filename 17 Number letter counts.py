import time
start_time = time.time()

ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
tens = {1:3, 2:6, 3:6, 4:6, 5:5, 6:5, 7:7, 8:6, 9:5}
elevens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
sum_n = 0

def ten(num):
    n = 0
    if num<=9:
        n += ones[num]
    elif num>9 and num<20:
        n += elevens[num]
    else:
        n = tens[num//10] + ones[num%10]
    return n

def count(num):
    global sum_n
    if len(str(num)) <= 2:
        sum_n += ten(num)
    elif len(str(num)) == 3:
        sum_n = sum_n + ones[num//100] + 7 + ten(num%100) # 7---> len('hundred')
        if num%100 != 0:
            sum_n += 3    #3 ---> len('and') 
    elif len(str(num)) == 4:
        sum_n += ones[num//1000] + 8  # 8 ---> len('thousand')
        
for i in range(10001):
    count(i)
print(sum_n)

print("\n--- %s seconds ---" % (time.time() - start_time))