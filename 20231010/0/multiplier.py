from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)


print(multiplier("2.124", "3.451", float))
print(multiplier("2.4", "123.241", Decimal))
print(multiplier("1/6", "2/3", Fraction))
