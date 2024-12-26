from decimal import Decimal
x = Decimal('0.01')
for i in range(15):
    x += Decimal('0.01')
    print(x)