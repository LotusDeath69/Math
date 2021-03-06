from sympy import solve, nsolve
from sympy.abc import x, y
from sympy import Symbol
import math


def formatDecimal(z: object) -> object:
    try:
        z = ('%f' % z).rstrip('0').rstrip('.')
        return z
    except TypeError:
        return z


def linearEquation(equation):
    [answer] = solve(equation)
    print(formatDecimal(answer))


def nonLinearEquation(eq1, eq2):
    x = Symbol('x')
    y = Symbol('y')
    [ans1, ans2] = nsolve([eq1, eq2], [x, y], [1, 1])
    print(f'x = {formatDecimal(ans1)}, y = {formatDecimal(ans2)}')


nonLinearEquation(x + y - 2, 2 * x + 2 * y - 4)
