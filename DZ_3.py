positive = 0
negative = 0
print("Введите 15 чисел по порядку")
for i in range(15):
    num = int(input())
    if num > 0:
        positive += num
    if num < 0:
        negative += num
print("Сумма положительных чисел: " + str(positive) + "\nСумма отрицательных чисел: "+str(negative))
