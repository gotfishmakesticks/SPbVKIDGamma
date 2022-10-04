pos,neg = 0,0
print("Введите 15 чисел по порядку кроме нуля")
for i in range(15):
    inp = int(input())
    if inp > 0:
        pos += inp
    elif inp < 0:
        neg += inp
    else:
        print("У вас ноль! Переход хода...\nИтог:\nКол-во итераций: " + str(i) + "\nПоложительная сумма: " + str(pos) + "\nОтрицательная сумма: " + str(neg))
        quit()
print("Итог:\nКол-во итераций: 15\nПоложительная сумма: " + str(pos) + "\nОтрицательная сумма: " + str(neg))