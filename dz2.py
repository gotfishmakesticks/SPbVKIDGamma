a, b = int(input("Введите a: ")), int(input("Введите b: "))
print("Выберите действие:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Решение кв. уравнения\n")
inp = int(input())
if inp == 1:
    print("Результат: " + str(a + b))
if inp == 2:
    print("Результат: " + str(a - b))
if inp == 3:
    print("Результат: " + str(a * b))
if inp == 4:
    print("Результат: " + str(a / b))
if inp == 5:
    c = int(input("a =" + str(a) + ", b = " + str(b) + ", c = "))
    d = b * b - (4 * a * c)
    print("d = " + str(d) + ", x1 = " + str((-b + d ** 0.5)/(2 * a)) + ", x2 = " + str((-b - d ** 0.5)/(2 * a)))
else:
    print("В следующий раз повезёт!")
#не финальная версия, финальная версия разбросана по веткам.