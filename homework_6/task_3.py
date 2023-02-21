import math

def slovel_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c

    if d == 0:
        x1 = -b / (2*a)
        x2 = None
    elif d < 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    else:
        x1 = (-b - d ** - 0.5) / (2 * a)
        x2 = (-b + d ** - 0.5) / (2 * a)

    return x1, x2

def test():
    x1, x2 = slovel_quadratic_equation(1, 2, -3)
    print('x1 =', x1)
    assert x1 == -3
    print('x2 =', x2)
    assert x2 == 1