print("Введите два числа")
first, second, mult = int(input("Введите первый множитель: ")), int(input("Введите второй множитель: ")), 0

for i in range(second):
    mult += first
print('Произведение равно: '+ str(mult))