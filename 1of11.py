print("1) (101 + 0) / 3\n2) 3.0e-6 * 10000000.1\n3) true && true\n4) false && true\n5) (false && false) || (true && true)\n6) (false || false) && (true && true)\nВведите соответствующую одному из выражений букву: ")
choice = int( input() )
exponent = 0
result = 0
if choice == 1:
    result = (101 + 0)/3
if choice == 2:
    exponent = 3 * 10**-6
    result = exponent * 10000000.1
if choice == 3:
    result = True & True
if choice == 4:
    result = False & True
if choice == 5:
    result = (False & False) | (True & True)
if choice == 6:
    result = (False | False) & (True & True)
print("Значение выражения: " + str(result))