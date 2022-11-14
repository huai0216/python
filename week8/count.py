import random
c_array = [0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    count = random.randint(0,9)
    if count == 0:
        c_array[0] = c_array[0]+1
    elif count == 1:
        c_array[1] = c_array[1]+1
    elif count == 2:
        c_array[2] = c_array[2]+1
    elif count == 3:
        c_array[3] = c_array[3]+1
    elif count == 4:
        c_array[4] = c_array[4]+1
    elif count == 5:
        c_array[5] = c_array[5]+1
    elif count == 6:
        c_array[6] = c_array[6]+1
    elif count == 7:
        c_array[7] = c_array[7]+1
    elif count == 8:
        c_array[8] = c_array[8]+1
    elif count == 9:
        c_array[9] = c_array[9]+1

print(c_array)
for i in range(10):
    print("{} number {}".format(i, c_array[i]))

    
