def number(x):
    a = 0
    while x > 0:
        a += 1
        x = x // 10
    return a


x = int(input("Введите число: "))
a = number(x)
print("Количество цифр в числе " + str(x) + ": " + str(a))
