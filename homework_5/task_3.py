import math

radius = float(input('Please Enter the Radius of a Cone: '))
height = float(input('Please Enter the Height of a Cone: '))

l = math.sqrt(radius * radius + height * height)

SA = math.pi * radius * (radius + l)

Volume = (1.0/3) * math.pi * radius * radius * height

LSA = math.pi * radius  * l

print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
print(" The Surface Area of a Cone = %.2f " %SA)
print(" The Volume of a Cone = %.2f" %Volume)
print(" The Lateral Surface Area of a Cone = %.2f " %LSA)
