from fractions import Fraction

print(2 / 3 + 1)
# 1.6666666666666665

print(Fraction(2 / 3 + 1).limit_denominator())
# 5/3