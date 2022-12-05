import os
filename = (input("Enter a filename: "))
num_list = []
with open(filename) as f:
    for line in f:
        num_list.extend([int(i) for i in line.split()])

num = len(num_list)
total = sum(num_list)
av = total/num
print(num_list)
print("There are {} scores\n\
The total is {}\n\
The averae is {}".format(num, total, av))


