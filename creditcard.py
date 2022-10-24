import math
credit = eval(input("Enter a credit card number:"))
num = []

i=1
for i in range(17):
    ten = 10 ** i
    num.append(credit % ten)   
    credit = credit // ten
    print(credit)
    i += 1
    #print(num)