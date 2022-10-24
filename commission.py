import math

def computeCommision(salesAmount):
    if(salesAmount > 5000):
        if(salesAmount > 10000):
            money12 = salesAmount - 10000
            com8 = 5000 * 0.08
            com10 = 5000 * 0.1
            com12 = money12 * 0.12
            commision = com8 + com10 + com12
        else :
            money10 = salesAmount-5000
            com10 = money10 * 0.1
            com8 = 5000 * 0.08
            commision = com10 + com8
    else :
        commision = salesAmount * 0.08
    print('{}\t\t{}'.format(salesAmount, commision))
    
print('Sales Amount\tCommision')
for i in range (10000, 100001, 5000):
    computeCommision(i)
