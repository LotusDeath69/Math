def checkConsistency(values, mode):
    # Find if the change of x is consistent
    # Mode: 1 = linear; 2 = quadratic; 3 = cubic
    consistency = True
    difference_x = []
    number = len(values) - 1
    for _ in values:
        i = values[number] - values[number - 1]
        difference_x.append(i)
        number -= 1
        if number == len(values) - 1:
            break

    if mode == 1:
        if difference_x[0] == difference_x[1]:
            pass
        else:
            consistency = False

    if mode == 2:
        if difference_x[0] == difference_x[1]:
            pass
        else:
            consistency = False
    if mode == 3:
        if difference_x[0] == difference_x[1]:
            if difference_x[2] == difference_x[3]:
                if difference_x[0] == difference_x[3]:
                    pass
                else:
                    consistency = False
            else:
                consistency = False
        else:
            consistency = False
    if consistency is False:
        print('the change in x is not constant \n'
              'Please try again!')
        quit()


def formatDecimal(x: object) -> object:
    try:
        x = ('%f' % x).rstrip('0').rstrip('.')
        return x
    except TypeError:
        return x


def formatInt(x: object) -> object:
    if x == 1:
        x = ''
    elif x == -1:
        x = '-'
    return x


def Linear(x1, y1, x2, y2, x3, y3):
    Formatting = True
    Verify = True
    PrintDifference = False
    # Linear Sequence:
    # y = a*n + constant
    # a = first difference between y2 and y1
    # solve for constant via substitution
    MODE = 1

    "# Check for consistency between the x values"
    values = [x1, x2, x3]
    checkConsistency(values, MODE)

    '# Find the rate of change of y values'
    y_values = [y3, y2, y1]
    iterator = 0
    difference = []
    for _ in y_values:
        i = y_values[iterator] - y_values[iterator + 1]
        difference.append(i)
        iterator += 1
        if iterator == 2:
            break
    if difference[0] != difference[1]:
        print('Not a linear sequence \n'
              'Please try again')

    '# Find the constant'
    a = difference[0]
    constant = -a * x1 + y1

    '# Format and/or print'
    if Formatting:
        print(f'sequence = {formatDecimal(formatInt(a))}n + {formatDecimal(formatInt(constant))}')
    else:
        print(f'sequence = {a}n + {constant}')

    '# Verifying'
    if Verify:
        y_values = [y3, y2, y1]
        iterator = 0
        difference = []
        for _ in y_values:
            i = y_values[iterator] - y_values[iterator + 1]
            difference.append(i)
            iterator += 1
            if iterator == 2:
                break
        constant = -a * x1 + y1
        if difference[0] * x3 + constant == y3:
            print('Verified')
        else:
            print('Cannot verify')

    '# Print the difference'
    if PrintDifference:
        print(f'Difference: {difference[0]}')


def Quadratic(x1, y1, x2, y2, x3, y3):
    PrintDifferences = False
    Verify = True
    Formatting = True
    # Quadratic Sequences:
    # a = 1/2 second differences
    # b = y2 - y1 - 3*a
    # c = y1 - b - a
    MODE = 2

    '#Check the if the change in x is constant'
    values = [x1, x2, x3]
    checkConsistency(values, MODE)
    for i in values:
        if i == 0:
            print('x cannot be zero \n'
                  'Please try again')
            quit()

    '#Find the first and second differences in y'
    y_values = [y3, y2, y1]
    iterator = 0
    first_difference = []
    for _ in y_values:
        i = y_values[iterator] - y_values[iterator + 1]
        first_difference.append(i)
        iterator += 1
        if iterator == 2:
            break
    second_difference = first_difference[0] - first_difference[1]

    '# Find a, b, c'
    a = second_difference / 2
    b = y2 - y1 - 3 * a
    c = y1 - b - a
    val = [a, b, c]
    cpy_val = val.copy()

    '#Format and/or print the equation'
    if Formatting:
        operator1 = '+'
        operator2 = '+'
        if b < 0:
            operator1 = '-'
            b *= -1
        if c < 0:
            operator2 = '-'
            c *= -1
        elif c == 0:
            operator2 = ''
        print(f'{formatDecimal(formatInt(a))}x^2 {operator1} {formatDecimal(formatInt(b))}x {operator2} '
              f'{formatDecimal(c)} = y')
    else:
        print(f'{a}x^2 + {b}x + {c} = y')

    '#Print the verified message'
    if Verify:
        '# cpy_val[0] = a'
        '# cpy_val[1] = b'
        '# cpy_val[2] = c'
        if cpy_val[0] * x3 ** 2 + cpy_val[1] * x3 + cpy_val[2] == y3:
            print('Verified')
        else:
            for i in cpy_val:
                print(i)
            print(x3)
            print('Unable to verify')

    '#Print the Second Difference'
    if PrintDifferences:
        print(f'Second Difference: {second_difference}')


def Cubic(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    PrintDifferences = True
    Verify = True
    Formatting = True
    # Cubic Sequence:
    # 6a = third difference
    # 12a + 2b = the first 2nd difference
    # 7a + 3b + c = u2 - u1 (y2 - y1)
    # a + b + c + d = u1 (y1)
    MODE = 3

    """# Preliminaries:"""
    values = [x1, x2, x3, x4, x5]
    checkConsistency(values, MODE)

    '#Find the first, second, and third difference'
    y_values = [y5, y4, y3, y2, y1]
    first_difference = []
    second_difference = []
    third_difference = []
    iterator = 0
    for _ in y_values:
        i = y_values[iterator] - y_values[iterator + 1]
        first_difference.append(i)
        iterator += 1
        if iterator == 4:
            iterator = 0

            for _ in first_difference:
                i = first_difference[iterator] - first_difference[iterator + 1]
                second_difference.append(i)
                iterator += 1
                if iterator == 3:
                    iterator = 0
                    for _ in second_difference:
                        i = second_difference[iterator] - second_difference[iterator + 1]
                        third_difference.append(i)
                        iterator += 1
                        if iterator == 2:
                            if third_difference[0] != third_difference[1]:
                                print('Not a Cubic Sequence \n'
                                      'Please try again')
                                quit()
                            break
                else:
                    continue
                break
        else:
            continue
        break

    '# Find the values of a, b, c, d'
    a = third_difference[0]/6
    b = (second_difference[2] - 12 * a) / 2
    c = (y2 - y1) - 7 * a - 3 * b
    d = y1 - a - b - c

    '# Format and/or print'
    if Formatting:
        print(f'{formatDecimal(formatInt(a))}x^3 + {formatDecimal(formatInt(b))}x^2 + {formatDecimal(formatInt(c))}x +'
              f' {formatDecimal(formatInt(d))} = y')
    else:
        print(f'{a}x^3 + {b}x^2 + {c}x + d = y')

    if Verify:
        a = third_difference[0] / 6
        b = (second_difference[2] - 12 * a) / 2
        c = (y2 - y1) - 7 * a - 3 * b
        d = y1 - a - b - c
        if a * x5 ** 3 + b * x5 ** 2 + c * x5 + d == y5:
            print('Verified')
        else:
            print('Cannot verified')

    if PrintDifferences:
        print(f'Third Difference: {third_difference[0]}')


Quadratic(1, 4, 2, 6, 3, 6)