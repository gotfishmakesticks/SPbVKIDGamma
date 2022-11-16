l = [int(input('Введите число ' + str(i + 1) + ': ')) for i in range(int(input('Количество чисел в списке: ')))]
l.sort()
check = True

for j in range(len(l)):
    if j == 0:
        if l[j] == l[j + 1]:
            check = False
    elif j == len(l) - 1:
        if l[j] == l[j - 1]:
            check = False
    else:
        if l[j] == l[j - 1] or l[j] == l[j + 1]:
            check = False

if check == True:
    print('Все числа являются уникальными.')
else:
    print('Присутствуют неуникальные числа.')