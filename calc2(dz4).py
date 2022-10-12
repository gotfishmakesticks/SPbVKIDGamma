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

numbers, oper = input('Введите числа через пробел: ').split(), input('Какая операция вас интересует?\n(+) - сложение\n(-) - отрицание\n(*) - умножение\n(/) - деление\n')

if len(numbers) < 2:
    print('Вы ввели меньше 2 чисел для примера! Пример не может быть решён!')
else:
    if oper == '+':
        print('Сумма равна: ' + str(summ(numbers)))
    elif oper == '-':
        print('Вычитание равна: ' + str(sub(numbers)))
    elif oper == '*':
        print('Произведение равна: ' + str(mult(numbers)))
    elif oper == '/':
        print('Деление равна: ' + str(div(numbers)))
    else:
        print('Некорректный ввод')