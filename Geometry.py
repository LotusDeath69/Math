import math
from fractions import Fraction
from sympy.core.symbol import Symbol
from Slope import *
from EquationSolver import nonLinearEquation

def DistanceFormula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def MidPointOfALine(x1, y1, x2, y2):
    return (x1 + x2)/2, (y1 + y2)/2


def EndPointOfALine(end_point1, end_point2, mid_point1, mid_point2):
    return -end_point1 + mid_point1 * 2, -end_point2 + mid_point2 * 2


def MixedFractionIntoImproper(a, b, c): 
    return f"{a*c+b}/{c}"


def ImproperFractionIntoMixed(a, b):
    return f"{a//b},{a%b}/{b}"


def DecimalIntoFraction(x):
    return Fraction(x)


def CircleEquation(x, y):
    return x**2+y**2


def AreaOfCircle(r):
    return r**2*3.14


def CircumferenceOfCircle(r):
    return r*2*3.14


def Centroid(x1, y1, x2, y2, x3, y3):
    return (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3


def PerpendicularBisector(x1, y1, x2, y2, default=True):
    (x, y), m = MidPointOfALine(x1, y1, x2, y2), negativeReciprocal(slopeLinear(x1, y1, x2, y2, default=False)[0])
    if default:
        f"y = {m}x + {Yintercept(x, y, m)}"
    return m, Yintercept(x, y, m)


def circumcenter(x1, y1, x2, y2, x3, y3):
    (eq1), (eq2), x, y = PerpendicularBisector(x1, y1, x2, y2, default=False), PerpendicularBisector(x2, y2, x3, y3, default=False), Symbol("x"), Symbol("y")
    x, y = nonLinearEquation(eq1[0]*x+eq1[1]-y,eq2[0]*x+eq2[1]-y)
    return (x, y)


def altitudesTriangle(x1, y1, x2, y2, x3, y3):
    return threeSlopes(x1, y1, x2, y2, x3, y3)


def threeDistanceFormula(x1, y1, x2, y2, x3, y3):
    return DistanceFormula(x1, y1, x2, y2), DistanceFormula(x2, y2, x3, y3), DistanceFormula(x3, y3, x1, y1)


def negativeReciprocal(x):
    if x != 0:
        return 1 / x * -1
    return 0


def triangleType(m1, m2, m3, length1, length2, length3):
    if negativeReciprocal(m1) == m2 or negativeReciprocal(m3) == m2 or negativeReciprocal(m1) == m3:
        return "Right triangle"
    elif length1 in [length2, length3] or length3 in [length1, length2]:
        if (m1 + m2 + m3)/3 == m1:
            return "Equalateral"
        return "Isoscele"
    return "Scalene"


def threeSlopes(x1, y1, x2, y2, x3, y3):
    return slopeLinear(x1, y1, x2, y2), slopeLinear(x2, y2, x3, y3), slopeLinear(x3, y3, x1, y1)


def Yintercept(x, y, slope):
    b = -1 * slope * x + y
    return b

if __name__ == "__main__":
    print(circumcenter(-2, 0, 2, 8, 7, 3))
