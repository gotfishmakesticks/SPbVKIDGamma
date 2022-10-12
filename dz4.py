#Создайте функцию для поиска минимума среди трех чисел (три параметра функции).
def min3(a, b, c):
    if a <= b:
        if a < c:
            return a
        else:
            return c
    elif b <= c:
        return b
    else:
        return c

def dignums(a):
    b = 0
    temp = []
    while a > 0:
        temp.append(a%10)
        a //= 10
        b += 1
    return "В числе " + str(b) + " цифр\nЦифры числа: " + str(list(reversed(temp)))

def sum(a):
    s = 0
    for i in range(a+1):
        s += i
    return s

def fact(a):
    f = 1
    for i in range(a):
        f *= i+1
    return f

loop = 0
state = 0
while state != -1:
    if state == 0:
        print("Выберите действие:\n1 - Сравнение 3 чисел\n2 - Вычислить кол-во цифр числа N\n3 - Сумма всех чисел от 1 до N\n4 - Факториал N\n-1 - Выход из программы")
        loop = 1
        while loop:
            inp = input()
            if inp == "1":
                state = 1
                loop = 0
            elif inp == "2":
                state = 2
                loop = 0
            elif inp == "3":
                state = 3
                loop = 0
            elif inp == "4":
                state = 4
                loop = 0
            elif inp == "-1":
                state = -1
                loop = 0
            else:
                print("Неверный ввод")
    elif state == 1:
        print("Результат: " + str(min3(int(input("Введите 1 число ")), int(input("Введите 2 число ")), int(input("Введите 3 число ")))))
        state = 0
    elif state == 2:
        print(dignums(int(input("Введите число "))))
        state = 0
    elif state == 3:
        print("Результат: " + str(sum(int(input("Введите число ")))))
        state = 0
    elif state == 4:
        print("Результат: " + str(fact(int(input("Введите число ")))))
        state = 0