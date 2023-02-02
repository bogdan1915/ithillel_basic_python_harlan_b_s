from decimal import *

getcontext().prec = 7

amount = int(input('введіть кількість гривень: '))

currentUsd = Decimal(amount)/Decimal(36.5686)

print('Станом на 1 лютого 2023 року це становить ' + currentUsd.__round__(2).__str__() + ' Долари США')