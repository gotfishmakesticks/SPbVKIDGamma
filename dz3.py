bool_var = True

while bool_var:
    sum_pos, sum_neg = list(), list()
    print('Введите 15 чисел (положительных или отрицательных)')
    for inp_loop in range(15):
        while True:
            inp = int(input('Введите ' + str(inp_loop + 1) + ' число: '))
            if inp > 0:
                sum_pos.append(inp)
                break
            elif inp < 0:
                sum_neg.append(inp)
                break
            else:
                print('Неверный ввод, повторите ещё раз')

    print('\nСумма положительных чисел')
    for out in range(len(sum_pos)):
        if out != (len(sum_pos) - 1):
            print(str(sum_pos[out]) + ' + ', end='')
        else:
            print(str(sum_pos[out]) + ' = ' + str(sum(sum_pos)))

    print('\nСумма отрицательных чисел')
    for out in range(len(sum_neg)):
        if out != (len(sum_neg) - 1):
            print('(' + str(sum_neg[out]) + ') + ', end='')
        else:
            print('(' + str(sum_neg[out]) + ') = '+ str(sum(sum_neg)) + '\n')

    while True:
        choice = input('Хотите ли повторить работу программы? Введите y(yes) / n(no): ')
        if choice.lower() == 'y':
            print('\n\n')
            break
        elif choice.lower() == 'n':
            bool_var = False
            break
        else:
            print('Неверный ввод, повторите попытку')