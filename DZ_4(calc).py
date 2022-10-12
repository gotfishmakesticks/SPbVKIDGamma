def plus(n):
    x = int(n[0])
    for i in range(1, len(n)):
        x += int(n[i])
    return x


def minus(n):
    x = int(n[0])
    for i in range(1, len(n)):
        x -= int(n[i])
    return x


def multiply(n):
    x = int(n[0])
    for i in range(1, len(n)):
        x *= int(n[i])
    return x


def divide(n):
    x = int(n[0])
    for i in range(1, len(n)):
        if int(n[i]) == 0:
            print('На 0 делить нельзя, пропуск числа')
        else:
            x /= int(n[i])
    return x


def equation(n):
    print("Взяты первые 3 числа")
    d = int(n[1]) * int(n[1]) - (4 * int(n[0]) * int(n[2]))
    x1, x2, x = 0, 0, 0
    if d > 0:
        x1 = ((int(n[1]) * -1) + d ** 0.5) / (2 * int(n[0]))
        x2 = ((int(n[1]) * -1) - d ** 0.5) / (2 * int(n[0]))
        return x1, x2
    elif d == 0:
        x = (int(n[1]) * -1) / (2 * int(n[0]))
        return x
    elif d < 0:
        print("Корней нет!")




numbers, oper = input("Введите числа через пробел: ").split(), input("Выберите операцию:\n(+) - сложение\n(-) - отрицание\n(*) - умножение\n(/) - деление\n(^) - квадратное уравнение\n")

if len(numbers) < 2:
    print("Введено меньше 2 чисел для примера! Пример нерешаем!")
else:
    if oper == "+":
        print("Сумма равна: " + str(plus(numbers)))
    elif oper == "-":
        print("Разность равна: " + str(minus(numbers)))
    elif oper == "*":
        print("Произведение равно: " + str(multiply(numbers)))
    elif oper == "/":
        print("Частное равно: " + str(divide(numbers)))
    elif oper == "^":
        print(str("Корни уравнения: " + str(equation(numbers))))
    else:
        print("Некорректный ввод")