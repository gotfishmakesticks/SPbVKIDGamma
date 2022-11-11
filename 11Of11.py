print("Введите значения сторон треугольника (после ввода каждого из чисел нажмите Enter: ")
firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
result1 = firstNumber + secondNumber > thirdNumber
result2 = firstNumber + thirdNumber > secondNumber
result3 = secondNumber + thirdNumber > firstNumber
if result1 & result2 & result3 == True:
    print("Данные стороны могут образовать треугольник.")
else:
    print("Треугольник с данными сторонами не существует.")