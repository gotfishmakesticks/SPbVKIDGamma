def summa(n):
    x = 0
    for i in range(1, n+1):
        x += i
    return x


n = int(input("Введите наибольшее число: "))
x = summa(n)
print("Сумма чисел от 1 до " + str(n) + ": " + str(x))
