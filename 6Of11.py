print("Введите два числа (после ввода каждого из чисел нажмите Enter): ")
firstNumber = int( input() )
secondNumber = int( input() )
result = 0
i = 0
for i in range(secondNumber):
    result = result + firstNumber
print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(result))