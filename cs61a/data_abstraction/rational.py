# An abstracted data type let us manipulate compound object as units
# We isolate two parts of any program
# How data are represented
# How data are manipulated
from math import gcd


RationalType = list[int]

# Rational representation and operation layer
def Rational(n: int, d: int) -> list[int]:
    """Contructor: use lits as the data structure to represent rational"""
    g = gcd(n, d)
    return [n // g, d // g]


def numor(r: RationalType):
    """numerator selector"""
    return r[0]


def denom(r: RationalType):
    """denominator selector"""
    return r[1]


# Rational computation layer
def add_rational(r1: RationalType, r2: RationalType):
    return Rational(
        numor(r1) * denom(r2) + numor(r2) * denom(r1),
        denom(r1) * denom(r2)
    )


def mul_rational(r1, r2):
    return Rational(
        numor(r1) * numor(r2), 
        denom(r1) * denom(r2)
    )


r1 = Rational(3, 5)
r2 = Rational(2, 3)
print(mul_rational(r1, r2))
