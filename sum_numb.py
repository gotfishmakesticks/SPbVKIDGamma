def sum_numb(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ

print('Сумма равна: ' + str(sum_numb( int(input('Введите число, с которым должны быть произведена сумма n (n > 0): ')) )))