# Проверка на отсутствие элементов внутри списка 1 к списку 2
import random

list1 = [random.randint(0, 100) for i in range(int(input('Сколько элементов в списке вы хотите видеть: ')))]
list2 = [random.randint(0, 100) for i in range(int(input('Сколько элементов в списке вы хотите видеть: ')))]
list_output, amount = [], 0

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            amount += 1
    if amount > 0:
        list_output.append(list1[i])
        amount = 0

print('Первый список: ' + str(list1))
print('Второй список: ' + str(list2))
print('Совпадающие числа: ' + str(list_output))