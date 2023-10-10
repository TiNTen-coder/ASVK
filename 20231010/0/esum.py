from decimal import Decimal, getcontext


def esum(N, one):
    ans = type(one)(1)
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
        ans += type(one)(1 / factorial)
    return ans


getcontext().prec = 100
print(esum(100, 1.0))
print(esum(100, Decimal("1.0")))
