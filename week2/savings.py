amount = eval(input('Enter monthly saving amount:'))
MonthRate = 0.05/12
month1 = (amount*(1+MonthRate))
month2 = ((amount+month1)*(1+MonthRate))
month3 = ((amount+month2)*(1+MonthRate))
month4 = ((amount+month3)*(1+MonthRate))
month5 = ((amount+month4)*(1+MonthRate))
month6 = ((amount+month5)*(1+MonthRate))
print('After the six month, the amount values is:',month6)