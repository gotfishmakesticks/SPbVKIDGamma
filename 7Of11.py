array = [76, 12, 2, 107, 53, 82, 143, 52, 97, 32, 121, 109, 66]
print("Массив array: " + str(array))
amount = 0
i = 0
#Считаем количество чисел в массиве array
for i in range(len(array)):
    amount = amount + 1
#Создаём два новые массива для чётных (even) и нечётных (uneven) чисел
even = []
uneven = []
i = 0
#Распределяем числа массива array путём проверки остатка от деления каждого из чисел на 2
for i in range(amount):
    if array[i] % 2 == 0 :
        even.append(array[i])
    else:
        uneven.append(array[i])
print("Чётные числа массива array: " + str(even) + "\nНечётные числа массива array: " + str(uneven))