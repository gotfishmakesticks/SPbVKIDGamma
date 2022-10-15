even, odd = list(), list()

while True:
    inp = int(input("Введите число (0 - окончание ввода): "))
    if inp == 0:
        break
    elif inp % 2 == 0:
        even.append(inp)
    elif inp % 2 != 0:
        odd.append(inp)
    else:
        print("Неправильный ввод")

print("Чётные числа: " + str(even) + "\nНечётные числа: " + str(odd))