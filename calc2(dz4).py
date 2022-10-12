def summ(n):
    ans = int(n[0])
    for i in range(1, len(n)):
        ans += int(n[i])
    return ans

def sub(n):
    ans = int(n[0])
    for i in range(1, len(n)):
        ans -= int(n[i])
    return ans

def mult(n):
    ans = int(n[0])
    for i in range(1, len(n)):
        ans *= int(n[i])
    return ans

def div(n):
    ans = int(n[0])
    for i in range(1, len(n)):
        if int(n[i]) == 0:
            print('Ноль нельзя, поэтому его в расчёт не берём')
        else:
            ans /= int(n[i])
    return ans

def quad(n):
    a, b, c = n
    a, b, c = int(a), int(b), int(c)
    dis = (b ** 2) - (4 * a * c)
    x1 = ((-b + (dis ** 0.5))) / (2 * a)
    if dis > 0:
        x2 = ((-b - (dis ** 0.5)) / (2 * a))
        return [x1, x2]
    elif dis == 0:
        return [x1]
    else:
        return ['Корней нет']

numbers, oper = input('Введите числа через пробел (для квадратного уравнения введите a, b, c): ').split(), input('Какая операция вас интересует?\n(+) - сложение\n(-) - отрицание\n(*) - умножение\n(/) - деление\n(q) - решение квадратного уравнения\n')

if len(numbers) < 2:
    print('Вы ввели меньше 2 чисел для примера! Пример не может быть решён!')
else:
    if oper == '+':
        print('Сумма равна: ' + str(summ(numbers)))
    elif oper == '-':
        print('Вычитание равно: ' + str(sub(numbers)))
    elif oper == '*':
        print('Произведение равно: ' + str(mult(numbers)))
    elif oper == '/':
        print('Частное равно: ' + str(div(numbers)))
    elif oper.lower() == 'q':
        perf = quad(numbers)
        if len(perf) == 2:
            print('x1 = ' + str(perf[0]) + ', x2 = ' + str(perf[1]))
        elif perf[0] == 'Корней нет':
            print(perf[0])
        else:
            print('x = ' + str(perf[0]))
    else:
        print('Некорректный ввод')
