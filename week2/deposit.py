finalAccountValue = eval(input('Enter final account value: '))
YearlyInterestRate = eval(input('Enter annual interest rate in percent: '))
numberofYears = eval(input('Enter number of years: '))
numberofMonths = 12*numberofYears
MonthlyInterestRate = YearlyInterestRate/1200
initialDepositAmount = finalAccountValue/((1+MonthlyInterestRate)**numberofMonths)
print('initial deposit value is ',round(initialDepositAmount))