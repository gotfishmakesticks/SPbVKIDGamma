inp = input('Нужно ли решать квадратное уравнение?\nВведите y(yes)/ n(no)\n')

if inp.lower() == 'y':

    a, b, c = input('Введите 3 числа через пробел. Пример: 5 -1 4\n').split()
    a, b, c = int(a), int(b), int(c)

    dis = (b ** 2) - (4 * a * c)

    x1 = ((-b + (dis ** 0.5))) / (2 * a)

    if dis > 0:
        x2 = ((-b - (dis ** 0.5)) / (2 * a))
        print('x1 = ' + str(x1) + ', x2 = ' + str(x2))
    elif dis == 0:
        print('x = ' + str(x1))
    else:
        print('Корней нет')

elif inp.lower() == 'n':

    print('Примечание!!\nПример вводиться строго через пробелы.\nПример: 55 / 11\n')

    fir, oper, sec = input('Введите пример (только одна операция)\nДоступные операции:\n(+) - сложение\n(-) - вычитание\n(*) - умножение\n(/) - деление\n').split()
    fir, sec = int(fir), int(sec)

    if oper == '+':
        print(fir + sec)
    elif oper == '-':
        print(fir - sec)
    elif oper == '*':
        print(fir * sec)
    elif oper == '/':
        if sec == 0:
            print('Деление на ноль невозможно')
        else:
            print(fir / sec)
    else:
        print('Недопустимый ввод')

else:
    print('Ввод был не верен, попробойте снова')