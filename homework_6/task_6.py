def sign_x(x):
    if x > 0:
        sing = 1
    elif x < 0:
        sing = -1
    else:
        sing = 0

    return sing


def test():
    result = sing_x(-365)
    print("Sing =", result)
    assert result == -1

    result = sing_x(421)
    print("Sing =", result)
    

