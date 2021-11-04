from Slope import *

def checkDifference(numbers, mode="linear"):
    difference = []
    for i in range(len(numbers) - 1):
        difference.append(numbers[i+1] - numbers[i])
    if mode == "quadratic":
        return checkDifference(difference)
    if mode == "cubic":
        return checkDifference(difference, mode="quadratic")
    if sum(difference)/len(difference) == difference[0]:
        if mode == "linear":
            return difference
        return True
    return False


def verify(val, var, mode="linear"):
    if mode == "linear":
        if not val[1] == var[0] * val[0] + var[1]:
            return False
    elif mode == "quadratic":
        if var[0] == 0:
            print("Not a quadratic system")
            quit()       
        if not val[1] == var[0] * val[0] ** 2 + var[1] * val[0] + var[2]:
            return False
    elif mode == "cubic":
        if not val[1] == var[0] * val[0] ** 3 + var[1] * val[0] ** 2 + var[2] * val[0] + var[3]:
            return False
    return True


def linear(x1, y1, x2, y2, x3, y3):
    numbers = [x1, y1, x2, y2, x3, y3]
    m, b = slopeLinear(x1, y1, x2, y2, default=False)
    for i in range(0, 6, 2):
        if not verify([numbers[i], numbers[i+1]], [m, b]):
            return "Not a linear system"
    return f"y = {m}x + {b}"


def quadratic(x1, y1, x2, y2, x3, y3):
    numbers = [x1, y1, x2, y2, x3, y3]
    if not checkDifference([x1, x2, x3]):
        return "Differences between x values are not consistent. \n Please try again."
    a = checkDifference([y1, y2, y3], mode="quadratic")[0] / 2 
    b = y2 - y1 - 3*a
    c = y1 - b - a 
    for i in range(0, 6, 2):
        if not verify([numbers[i], numbers[i+1]], [a, b, c], mode="quadratic"):
            print("Unable to verify")
    if not verify([x3, y3], [a, b, c], mode="quadratic"):
        print("Unable to verify")
    return f"y = {a}x^2 + {b}x + {c}"


def cubic(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    numbers = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
    if not checkDifference([x1, x2, x3, x4, x5]):
        return "Differences between x values are not consistent. \n Please try again."
    a = checkDifference([y1, y2, y3, y4, y5], mode="cubic")[0] / 6
    b = (y3 - 2 * y2 -y1) / 2
    c = (y2 - y1) - 7 * a - 3 * b
    d = y1 - a - b - c
    for i in range(0, 10, 2):
        if not verify([numbers[i], numbers[i+1]], [a, b, c, d], mode="cubic"):
            print("Unable to verify")
    return f"y = {a}x^3 + {b}x^2 + {c}x + {d}"



# print(linear(1, 4, 2, 6, 3, 8))
print(quadratic(4, -1, 5, 3, 6, -1))
# print(cubic(1, 3, 2, 6, 3, 12, 4, 24, 5, 45))

