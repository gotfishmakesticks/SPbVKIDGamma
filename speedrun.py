from random import random
import math
#Выполнили Мартин Ярослав и Миренков Алексей
state = 0
def inputer():
    print("Введите что угодно, чтобы продолжить")
    inp = input()
    global state
    state = 0
while state != -1:
    if state == 0:
        print("Главное меню\nВвод от 1 до 11 - выбор задания\n-1 завершит работу программы")
        inp = int(input("Вводите, сударь!\n"))
        state = inp
    elif state == 1:
        print((101+0)/3)
        print(3.0e-6*1000000.1)
        print(True and True)
        print(False and True)
        print(((False and False) or (True and True)))
        print(((False or False) and (True and True)))
        inputer()
    elif state == 2:
        print("Введите 4 числа через 1 пробел каждое")
        a = input().split(" ", 4)
        for i in range(4):
            a[i] = int(a[i])
        print("Вы ввели " + str(a))
        if a[0] == a[1] == a[2] == a[3]:
            print("Числа равны друг другу, ура!")
        else:
            print("Увы, числа не равны друг другу :с")
            inputer()
    elif state == 3:
        b = []
        for i in range(20):
            b.append(round(random() * 100))
        print("Вот ваш так называемый массив: " + str(b))
        print("Введите, сколько наибольших чисел вы хотите (прошу не меньше 0 и не больше 20)")
        inp = int(input())
        if inp < 0:
            print("Ну я же просил! Ладно, будет вам 0")
            inp = 0
        elif inp > 20:
            print("Ну я же просил! Ладно, будет вам 20")
            inp = 20
        b.sort(reverse = True)
        print("Вот ваши числа:")
        for i in range(inp):
            print(b[i])
        inputer()
    elif state == 4:
        c = []
        for i in range(20):
            c.append(round(random() * 100))
        print("Вот ваш так называемый массив: " + str(c))
        print("Введите, сколько наименьших чисел вы хотите (прошу не меньше 0 и не больше 20)")
        inp = int(input())
        if inp < 0:
            print("Ну я же просил! Ладно, будет вам 0")
            inp = 0
        elif inp > 20:
            print("Ну я же просил! Ладно, будет вам 20")
            inp = 20
        c.sort()
        print("Вот ваши числа:")
        for i in range(inp):
            print(c[i])
        inputer()
    elif state == 5:
        d = []
        print("Нам потребуется от вас небольшая помощь...Введите кол-во чисел в массиве, не меньше одного >> ")
        inp = int(input())
        e = 0
        if inp < 1:
            print("Эх...ладно...будет 1")
            inp = 1
        for i in range(inp):
            d.append(round(random() * 100))
            e += d[i]
        e = e / inp
        f = []
        for i in range(inp):
            if d[i] >= e:
                f.append(d[i])
        print("Ср. ариф: " + str(e) + "\nНачальный массив: " + str(d) + "\nЧисла, больше ср.ариф.: " + str(f))
        inputer()
    elif state == 6:
        print("Введите 2 числа через 1 пробел")
        g = input().split(" ", 2)
        for i in range(2):
            g[i] = int(g[i])
        print("Вы ввели " + str(g))
        h = g[0] / math.pow(g[1], -1)
        print("Вот ваше так называемое умножение через деление: " + str(h))
        inputer()
    elif state == 7:
        print("Введите длину массива, не меньше 1 пожалуйста")
        inp = int(input())
        if inp < 1:
            print("Я же просил :с, пусть тогда будет 1")
            inp = 1
        j = []
        for i in range(inp):
            j.append(round(random() * 100))
        k = []
        l = []
        for i in range(inp):
            if j[i] % 2 == 0:
                k.append(j[i])
            else:
                l.append(j[i])
        print("Вот ваши массивы:\nОригинальный - " + str(j) + "\nЧётный - " + str(k) + "\nНечётный - " + str(l))
        inputer()
    elif state == 8:
        print("Введите температуру в Фаренгейтах")
        inp = int(input())
        inp = (inp - 32) / 1.8
        print("Вот ваши " + str(inp) + "°С")
        inputer()
    elif state == 9:
        print("Введите вес (в кг) и рост (в см) через 1 пробел")
        m = input().split(" ", 2)
        for i in range(2):
            m[i] = int(m[i])
        print("Вы ввели:\n" + str(m[0]) + " кг - Вес\n" + str(m[1]) + " см - Рост")
        n = m[0] / ((m[1]/100)**2)
        print("Ваш ИМТ: " + str(n))
        inputer()
    elif state == 10:
        print("Введите число, абсолютно любое!")
        inp = int(input())
        o = []
        for i in range(4):
            o.append(inp ** (i+1))
        print("Вот ваши 1-4 степени, слева направо: " + str(o))
        inputer()
    elif state == 11:
        print("Введите 3 числа через 1 пробел каждое")
        p = input().split(" ", 3)
        for i in range(3):
            p[i] = int(p[i])
        p.sort(reverse = True)
        if p[0] > (p[1] + p[2]):
            print("Треугольнику быть")
        else:
            print("У меня для вас плохие новости...")
        inputer()
    else:
        print("Неверный ввод")
        inputer()