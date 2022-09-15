import math
x1 = eval(input('x1:'))
y1 = eval(input('y1:'))
print("address 1 is : (",x1, ',',y1,")")
x2 = eval(input('x2:'))
y2 = eval(input('y2:'))
print("address 2 is : (",x2, ',',y2,")")
dis = math.sqrt((x2-x1)**2+(y2-y1)**2)

print('distance between two address is :%.4f'%dis)
