import random

amount, s, sum_numb = int(input('Сколько чисел хотите в массиве? ')), list(), 0
mid, mid_top = 0, list()

for i in range(amount):
    inp = random.randint(0, 10000)
    s.append(inp)
    sum_numb += inp

mid = sum_numb / len(s)

for i in range(len(s)):
    if s[i] > mid:
        mid_top.append(s[i])
print('Все числа списка: ' + str(s))
print('Среднее число всех чисел списка: ' + str(mid))
print('Числа, превышающие среднее число: ' + str(mid_top))