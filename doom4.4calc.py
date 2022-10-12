a, b = int(input("Enter a: ")), int(input("Enter b: "))
d = 0
def sum(a, b):
    return a+b
def min(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def discr(d):
    c = int(input("a =" + str(a) + ", b = " + str(b) + ", c = "))
    d = b * b - (4 * a * c)
    if d < 0:
        print("\nДискриминант комплексный")
        quit()
    elif d == 0:
        print("\nd = " + str(d) + "\nx = " + str(-b / (2 * a)))
        quit()
    else:
        print("\nd = " + str(d) + "\nx1 = " + str((-b + d ** 0.5) / (2 * a)) + "\nx2 = " + str((-b - d ** 0.5) / (2 * a)))
        quit()
    return d
print("\nChoose to use:\n1 - Sum\n2 - Substraction\n3 - Multiplication\n4 - Division\n5 - Quadratic equation\n")
temp = int(input())
if temp == 1:
    print("\nResult: " + str(sum(a,b)))
if temp == 2:
    print("\nResult: " + str(min(a,b)))
if temp == 3:
    print("\nResult: " + str(mult(a,b)))
if temp == 4:
    print("\nResult: " + str(div(a,b)))
if temp == 5:
    print("\nResult: " + str(discr(d)))