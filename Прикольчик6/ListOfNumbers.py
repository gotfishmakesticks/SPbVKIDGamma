# Ввод чисел и вывод их списком
def separator(numbs):
    output, numb = [], ''
    for symbol in range(len(numbs)):
        if symbol != len(numbs) - 1:
            if numbs[symbol] != ',':
                numb += numbs[symbol]
            else:
                #Ввод в список
                output.append(int(numb))
                numb = ''
        else:
            if numbs[symbol] != ',':
                numb += numbs[symbol]
            output.append(int(numb))

    return output

print(separator(input('Введите числа через запятую (без пробела): ')))