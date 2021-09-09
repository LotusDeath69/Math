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
    [ans1, ans2] = nsolve([eq1, eq2], [x, y], [1, 1])
    return int(formatDecimal(ans1)), int(formatDecimal(ans2))

if __name__ == "__main__":  
    nonLinearEquation(x + y - 2, 2 * x + 2 * y - 4)
