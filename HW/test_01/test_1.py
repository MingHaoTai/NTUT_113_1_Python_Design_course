#2024-09-18
#負數不用四捨五入??
import math

a = int(input())
b = int(input())
c = int(input())
x1 = float((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
x2 = float((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

if (x1 * 100) % 10 >= 5:
    if x1 >= 0:
        x1 = x1 + 0.1
    else:
        x1 = x1
if (x2 * 100) % 10 >= 5:
    if x2 >= 0:
        x2 = x2 + 0.1
    else:
        x2 = x2

if x1 == x2:
    print("%.1f" %x1)
else:
    print("%.1f" %x1)
    print("%.1f" %x2)
