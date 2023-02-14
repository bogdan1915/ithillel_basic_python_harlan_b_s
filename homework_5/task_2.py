def area(a, b, c):

    s = (a + b + c) / 2

    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

def perimeter(a, b, c):

    perim = a + b + c
    return perim

def main():
    a = int(input('Enter first side: '))
    b = int(input('Enter second side: '))
    c = int(input('Enter third side: '))

    print( "Area is:", area(a, b, c))
    print("Perimeter is:", perimeter(a, b, c))

main()

