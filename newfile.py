from fish import intinput, clamp
a = []
b = []
from random import random, randint
for i in range(randint(1, 50)):
	a.append(round(random() * 100))
for i in range(randint(1, 50)):
	b.append(round(random() * 100))
print("A = " + str(a) + "\nB = " + str(b))
c = []
for i in range(len(a)):
	if a[i]%2 == 1:
		c.append(a[i])
for i in range(len(b)):
	if b[i]%2 == 0:
		c.append(b[i])
print("Задание 1")
print("C = " + str(c))
d = []
for i in range(1, len(c)+1):
	d.append(c[-i])
print("Задание 2")
print("Reversed C = " + str(d))
print("Задание 3, простые числа")
primes = []
nonprimes = []
print("Введите диапазон (мин. 2)")
inp = intinput()
diap = clamp(inp, 2, inp)
for i in range(2, diap+1):
	for j in range(2, diap+1):
		if (i%j == 0) and (i != j):
			nonprimes.append(i)
			break
		elif i == j:
			primes.append(i)
print("Простые числа диапазона:\n" + 
str(primes) + 
"\nОставшиеся числа:\n" +
str(nonprimes))
print("Задание 4, перевод числа в разн. с.с.")
print("Введите желаемое число")
inp = intinput()
print("Введите систему счисления")
ss = intinput()
ss = clamp(ss, 1, ss)
q = []
hexing = {10 : "A", 11 : "B"}
while inp > 0:
	q.append(inp % ss)
	inp = inp // ss
q.sort(reverse = True)
print("Результат (1 эл. списка - 1 \"цифра\"):\n" + str(q))
print("Задание 8")
num = int(input("Введите число"))
if num % 2 == 0:
    print("Число " + str(num) + " четное")
else:
    print("Число " + str(num) + " нечетное")
print("Задание 9")
print("Введите длину в футах и дюймах")
foot = int(input("Футы: "))
inch = int(input("Дюймы: "))
inch2 = inch + (foot * 12)
if inch2 > 400:
    print("Вы там что, Великую китайскую стену мерите?")
sm = inch2 * 2.54
print(str(foot) + " фт. " + str(inch) + " дюйм. = " + str(sm) + " см.")
print("Задание 10")
time = []
seltime = int(input("Выберите единицу времени:\n1 - секунды\n2 - минуты\n3 - часы\n4 - дни\n"))
if seltime == 1:
    numtime = int(input("Введите кол-во секунд: "))
    time.append(numtime)
    time.append(numtime/60)
    time.append(numtime/3600)
    time.append(numtime/86400)
    print(str(time[0]) + " сек. равно:\n" + str(time[1]) + " мин.\n" + str(time[2]) + " ч.\n" + str(time[3]) + " дн.")
elif seltime == 2:
    numtime = int(input("Введите кол-во минут: "))
    time.append(numtime * 60)
    time.append(numtime)
    time.append(numtime / 60)
    time.append(numtime / 1440)
    print(str(time[1]) + " мин. равно:\n" + str(time[0]) + " сек.\n" + str(time[2]) + " ч.\n" + str(time[3]) + " дн.")
elif seltime == 3:
    numtime = int(input("Введите кол-во часов: "))
    time.append(numtime * 3600)
    time.append(numtime * 60)
    time.append(numtime)
    time.append(numtime / 24)
    print(str(time[2]) + " ч. равно:\n" + str(time[0]) + " сек.\n" + str(time[1]) + " мин.\n" + str(time[3]) + " дн.")
elif seltime == 4:
    numtime = int(input("Введите кол-во дней: "))
    time.append(numtime * 86400)
    time.append(numtime * 3600)
    time.append(numtime * 60)
    time.append(numtime)
    print(str(time[3]) + " дн. равно:\n" + str(time[0]) + " сек.\n" + str(time[1]) + " мин.\n" + str(time[2]) + " ч.")
else:
    print("Некорректный ввод")