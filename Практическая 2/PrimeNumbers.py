check = int(input("Введите конец диапазона простых чисел: "))

list1 = [2]

amo = 0

for kak in range (2,check+1):
    for kak2 in range (2, kak+1):
        if kak %kak2 != 0:
            amo += 1
        elif kak%kak2 == 0 and kak != kak2:
            amo = 0
            break
    if amo > 0:
        list1.append(kak)

print(f'\nПростые числа в диапазоне от 2 до {check}: \n{list1}')