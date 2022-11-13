s = [6790, 25092, 7947, 13073, 18421, 10065, 22741, 7887, 22440, 335, 9493, 12921, 19176, 27484, 3128, 13227]
amount = 0
i = 0
#Считаем количество чисел в массиве
for i in range(len(s)):
    amount = amount + 1
print("Количество чисел массива s равно " + str(amount))
summation = 0
i = 0
#Находим среднее значение среди чисел массива s
for i in range(amount):
    summation = summation + s[i]
average = summation / amount
print("Cреднее значение среди чисел массива s равно " + str(average) + "\nСледующие числа массива s превышают среднее значение чисел массива:")
i = 0
for i in range(amount):
    if s[i] > average:
        print(s[i])