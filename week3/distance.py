import math
from math import cos as cos
from math import sin as sin
from math import acos as acos
x1,y1 = eval(input('Enter point 1(latitude and longitude) in degrees:'))
x2,y2 = eval(input('Enter point 2(latitude and longitude) in degrees:'))
radius = 6371.01
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
d = radius * acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print('The distance between the two point is ', d)