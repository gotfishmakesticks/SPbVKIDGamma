print("Введите число, факториал которого необходимо вычислить:")
number = int( input() )
factorial = 1
#Уменьшающемуся числу присваиваем значение данного числа
decreasingNumber = number
i = 0
for i in range(number):
    factorial = factorial * decreasingNumber
    decreasingNumber = decreasingNumber - 1
print("Факториал числа " + str(number) + " равен " + str(factorial))
