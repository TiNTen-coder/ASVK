from fractions import Fraction


def solve(s, w, *rest):
    a_power = int(rest[0])
    a_coeffs = rest[1:a_power + 2]
    b_power = int(rest[a_power + 2])
    b_coeffs = rest[-b_power - 1:]
    a_s = Fraction(0)
    for i in range(a_power + 1):
        a_s += a_coeffs[i] * s ** (a_power - i)
    b_s = Fraction(0)
    for i in range(b_power + 1):
        b_s += b_coeffs[i] * s ** (b_power - i)
    if not b_s:
        return False
    return a_s/b_s == w


print(solve(*map(Fraction, input().split(', '))))
