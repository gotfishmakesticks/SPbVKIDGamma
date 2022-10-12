def minim(first, second, third):
    min = first
    if second < min:
        min = second
    if third < min:
        min = third
    return min

print('Поиск минимального числа')
print('Минимальное число: ' + str(minim( int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')) )))