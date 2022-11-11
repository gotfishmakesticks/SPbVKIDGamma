print("Введите 3 числа (после ввода каждого из чисел нажмите Enter):")
#Сразу присваиваем переменной minimumNumber значение первого введённого числа вместо значения 0, чтобы остальные введённые числа сразу сравнивались с первым числом, а не с нулём
minimumNumber = int( input() )
inputNumber = 0
i = 0
#Цикл для остальных двух вводимых чисел
for i in range(2):
    inputNumber = int( input() )
    if inputNumber < minimumNumber:
        minimumNumber = inputNumber
print("Минимальное из данных чисел равно " + str(minimumNumber))