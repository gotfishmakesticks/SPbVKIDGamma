# Из двоичной в десятичную
def FromAnyToDecimal(numb, numb_sys):
    output, amount = 0, 0
    while numb != '':

        # Проверка на число
        if '0' <= numb[len(numb) - 1] <= '9':
            numb1 = int(numb[len(numb) - 1])
        else:
            numb1 = int(letters[numb[len(numb) - 1]])

        # Проверка на корректность ввода
        if numb1 >= numb_sys:
            return 'Ошибка! Число ' + str(numb1) + ' не может использоваться в ' + str(numb_sys) + '-чной системе счисления'

        output += numb1 * (numb_sys ** amount)
        numb = numb[:-1]
        amount += 1
    return output

def FromDecimalToAny(numb, numb_sys):
    output = ''
    numb = int(numb)
    while numb != 0:
        remainder = numb % numb_sys
        if remainder >= 10:
            for key, value in letters.items():
                if remainder == value:
                    output += key
        else:
            output += str(remainder)
        numb //= numb_sys
    return output[::-1]

# Словарь соотнесённых чисел к буквам
letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16,
           'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
           'O': 24, 'P': 25, 'Q': 26,'R': 27, 'S': 28, 'T': 29, 'U': 30,
           'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

# Ввод данных
numb = input('Введите число: ')
numb_sys_input = int(input('Введите систему счисления данного числа (для ввода используйте целое число, максимальное - 36): '))
numb_sys_output = int(input('Введите систему счисления, в которую нужно перевести (для ввода используйте целое число, максимальное - 36): '))

if numb_sys_input == numb_sys_output:
    print('А смысл в данном переводе?')
else:
    #Вызов нужной функции
    if numb_sys_input != 10 and numb_sys_output != 10:
        print('Результат:\n' + str(FromDecimalToAny(FromAnyToDecimal(numb, numb_sys_input), numb_sys_output)))
    elif numb_sys_output == 10:
        print('Результат:\n' + str(FromAnyToDecimal(numb, numb_sys_input)))
    elif numb_sys_input == 10:
        print('Результат:\n' + str(FromDecimalToAny(numb, numb_sys_output)))