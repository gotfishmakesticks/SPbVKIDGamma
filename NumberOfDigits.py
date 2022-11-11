print("Введите число и нажмите Enter:")
inputNumber = int( input() )
numberOfDigits = 0
#Целочисленно делим число на 10, пока оно не будет меньше нуля
while inputNumber > 0:
    inputNumber = inputNumber//10
    #После каждого деления прибавляем к количеству цифер единицу
    numberOfDigits = numberOfDigits + 1
print("Количество цифер в данном числе равно " + str(numberOfDigits))