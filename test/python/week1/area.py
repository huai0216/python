import math
n = eval(input('poly : '))
s = eval(input('length : '))
area = (n*(s**2))/(4*math.tan(math.pi/n))
print("area is: %.4f"%area)
