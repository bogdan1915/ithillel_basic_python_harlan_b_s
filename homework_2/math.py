import math

a,b,c = 1,5,4

x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a)

print(x)

x= (-b - math.sqrt (b ** 2 - 4 * a * c)) / (2 * a)

print(x)


x= (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)

print(x)

x = (-b -((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)

print(x)
