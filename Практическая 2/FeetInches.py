print("Пример: 15 ft 15 inch")
count = input("Введите число в имперской системе: ")

num1 = 0
num2 = 0

text = ""

for cy in range (len(count)):
    if "0"<=count[cy]<="9":
        text += count[cy]
    else:
        if text != "":
            if num1 == 0:
                num1 = int(text)
                text = ""
            else:
                num2 = int(text)

print(f'Ваша величина: {num1} футов, {num2} дюймов\n')

print("Переводим в сантиметры..\n")

sum = (num1 * 30.48) + (num2 * 2.54)

print(f'Итог: {sum} сантиметров')
