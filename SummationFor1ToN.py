print("Введите количество чисел: ")
amountOfNumbers = int( input() )
summation = 0
i=0
print("Введите все числа (после ввода каждого из чисел нажмите Enter):")
for i in range(amountOfNumbers):
    inputNumber = int( input() )
    summation = summation + inputNumber
print("Сумма данных чисел равна " + str(summation))