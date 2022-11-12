import random

def backword(l):
    list_bw = []
    for i in range(len(l)):
        list_bw.append(l[len(l) - 1 - i])
    return list_bw

amount = int(input('Сколько чисел хотите в массивах? '))
list_main = [[], []]

for i in range(amount):
    numb = random.randint(0, 1000)
    if numb % 2 != 0:
        list_main[0].append(numb)
    numb = random.randint(0, 1000)
    if numb % 2 == 0:
        list_main[1].append(numb)

print('Вывод нечётных: ')
for input_list_main_1 in range(len(list_main[0])):
    if input_list_main_1 != len(list_main[0]) - 1:
        print(list_main[0][input_list_main_1], end=', ')
    else:
        print(list_main[0][input_list_main_1])

print('Вывод чётных: ')
for input_list_main_2 in range(len(list_main[1])):
    if input_list_main_2 != len(list_main[1]) - 1:
        print(list_main[1][input_list_main_2], end=', ')
    else:
        print(list_main[1][input_list_main_2])

print('Нечётные в обратном порядке:', *backword(list_main[0]))
print('Чётные в обратном порядке:', *backword(list_main[1]))