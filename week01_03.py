# вычислить корни квадратного уравнения
# 04/10/2018

import sys
from math import sqrt
import requests

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print(str(int((-b+sqrt(pow(b, 2)-4*a*c))/(2*a))))
print(str(int((-b-sqrt(pow(b, 2)-4*a*c))/(2*a))))
print(requests)

