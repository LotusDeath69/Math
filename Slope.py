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


def slopeLinear(x1, y1, x2, y2, Formatting=True, Verify=False, default=True):
    # Linear Sequences:
    # Solve for slope via point-slope form
    # Solve for y-intercept by substistute in x and y values

    '#Preliminaries'
    if y2 == y1:
        return f'Zero Slope; \ny-intercept = {y1}'
    if x2 == x1:
        return "Undefined slope"


    '#Find the slope'
    m, a, b, = 0, x1-x2, y1-y2
    if a != 0:
        m = b / a

    '#Find the y-intercept'
    y_intercept = -m * x1 + y1
    if not default:
        return m, y_intercept
    if Verify:
        if not y2 == m * x2 + y_intercept:
            print('Cannot Verified equation')
    if Formatting:
        if y_intercept == 0:
            return f'y = {formatDecimal(formatInt(m))}x'
        else:
            if y_intercept < 0:
                return f'y = {formatDecimal(formatInt(m))}x - {formatDecimal(formatInt(y_intercept))}'
            else:
                return f'y = {formatDecimal(formatInt(m))}x + {formatDecimal(formatInt(y_intercept))}'
    else:
        return f'y = {m}x + {b}'
# slopeLinear(0, 500, 200, 7000)
