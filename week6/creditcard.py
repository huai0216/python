import math
credit = eval(input("Enter a credit card number:"))


def isValid(number):
    num = list(str(number))
    evensum = 0
    oddsum =  0
    for i in range(0,16,2):
        even = int(num[i]) * 2
        if(even > 9) :
            even10 = even //10
            even1  = even % 10
            even = even10 + even1
            evensum = even + evensum
        else :
            evensum = even + evensum
    for i in range(1, 17, 2):
        odd = int(num[i])
        oddsum = odd + oddsum
    return oddsum + evensum

if isValid(credit) %10 == 0:
    result = "valid"
else :
    result = "invalid"
print('The credit card {} is {}'.format(credit, result))