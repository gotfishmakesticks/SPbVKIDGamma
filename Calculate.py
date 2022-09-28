import math
print("Выберите действие:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Решение кв. уравнения\n")
inp = int(input())
if (1 <= inp <= 5) == False:
    print("Похоже, Вы не хотите считать.")
    quit()
if (1 <= inp <= 4):
    a, b = int(input("Введите a: ")), int(input("Введите b: "))
    if inp == 1:
        print("Результат: " + str(a + b))
    if inp == 2:
        print("Результат: " + str(a - b))
    if inp == 3:
        print("Результат: " + str(a * b))
    if inp == 4:
        print("Результат: " + str(a / b))
else:
    a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))
if inp == 5:
    d = b * b - (4 * a * c)
    if d < 0:
        print("Так как дискриминант меньше нуля, то уравнение не имеет корней.")
        quit()
    if d == 0:
        print("D= " + str(d) + ", x= " + str((-b)/(2 * a)))
        quit()
    print("D= " + str(d) + ", x1= " + str((-b + d ** 0.5)/(2 * a)) + ", x2= " + str((-b - d ** 0.5)/(2 * a)))