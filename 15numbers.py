print("Введите 15 чисел (после ввода каждого из чисел нажмите Enter):")
positiveSummation = 0
negativeSummation = 0
i = 0
for i in range(15):
    number = int( input() )
    #Проверка числа на положительность
    if number > 0:
        #Положительно - прибавляется к сумме положительных чисел
        positiveSummation = positiveSummation + number
    else:
        #Отрицательно - прибавляется к сумме отрицательных чисел
        negativeSummation = negativeSummation + number
print("Сумма положительных чисел равна " + str(positiveSummation) + "\nСумма отрицательных чисел равна " + str(negativeSummation))