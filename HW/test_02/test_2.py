#20024-09-18
import math

a = int(input())
b = int(input())
c = int(input())

#determine
if (b ** 2 - 4 * a * c) >= 0:
    determine = math.sqrt(b ** 2 - 4 * a * c)
    x1 = float((-b + determine) / (2 * a))
    x2 = float((-b - determine) / (2 * a))
    if (x1 * 100) % 10 >= 5:
        if x1 >= 0:
            x1 = x1 + 0.1
    if (x2 * 100) % 10 >= 5:
        if x2 >= 0:
            x2 = x2 + 0.1
    if x1 == x2:
        print("%.1f" %x1)
    else:
        print("%.1f" %x1)
        print("%.1f" %x2)
else:
    determine = math.sqrt(-(b ** 2 - 4 * a * c)) / abs(2 * a)
    x1 = float((-b) / (2 * a))
    # if (x1 * 100) % 10 >= 5:
    #     if x1 >= 0:
    #         x1 = x1 + 0.1
    print("%.1f+%.1fi" %(x1, determine))
    print("%.1f-%.1fi" %(x1, determine))