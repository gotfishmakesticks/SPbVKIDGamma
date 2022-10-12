def factorial(n):
    x = 1
    for i in range(1, n+1):
        x = x*i
    return x


n = int(input("Введите число: "))
x = factorial(n)
print("Факториал числа " + str(n) + ": " + str(x))
