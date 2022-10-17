decimal = eval(input('Enter a decimal value:'))
binary = ''
while decimal != 0:
    
    binary = str(decimal%2)+binary
    decimal =  decimal //2
    
   

print('The decimal value {} conver to binary is {}'.format(decimal,binary))