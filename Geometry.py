import math
from fractions import Fraction
from sympy.core.symbol import Symbol
from Slope import *
from EquationSolver import nonLinearEquation

def DistanceFormula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), f"sqrt {(x2-x1)**2+(y2-y1)**2}"


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
        return f"y = {m}x + {Yintercept(x, y, m)}"
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


def triangleType(x1, y1, x2, y2, x3, y3):
    a = threeSlopes(x1, y1, x2, y2, x3, y3, default=False)[::1]
    for i in a:
        print(i)
    # print(a)


def threeSlopes(x1, y1, x2, y2, x3, y3, default=True):
    if default:
        return slopeLinear(x1, y1, x2, y2), slopeLinear(x2, y2, x3, y3), slopeLinear(x3, y3, x1, y1)
    return slopeLinear(x1, y1, x2, y2, default=False), slopeLinear(x2, y2, x3, y3, default=False), slopeLinear(x3, y3, x1, y1, default=False)

def Yintercept(x, y, slope):
    return -1 * slope * x + y


def threeMidPoints(x1, y1, x2, y2, x3, y3):
    return MidPointOfALine(x1, y1, x2, y2), MidPointOfALine(x2, y2, x3, y3), MidPointOfALine(x3, y3, x1, y1)


def distanceLineAndPoint(m1, b1, x2, y2, default=True):
    m2 = negativeReciprocal(m1)
    b2, x, y = -m2*x2+y2, Symbol("x"), Symbol("y")
    x,y = nonLinearEquation(m1*x+b1-y,m2*x+b2-y)
    print(x, y, m2, b2)
    if default:
        return DistanceFormula(x, y, x2, y2), m2, b2, (x, y)
    return DistanceFormula(x, y, x2, y2)


def threePoints(x1, y1, x2, y2):
    (slope, b), increment, ans = slopeLinear(x1, y1, x2, y2, default=False), (x1 - x2) / 4, []
    for i in range(1, 4):
        ans.append((x1 - increment * i, (x1 - increment * i) * slope + b))
    return ans 

if __name__ == "__main__":
    print(DistanceFormula(-1, 4, 4, -1))