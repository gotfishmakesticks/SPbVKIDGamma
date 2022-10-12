def numb_of_dig(text):
    amount = 0
    for i in text:
        if '0' <= i <= '9':
            amount += 1
        else:
            amount = 'Ошибка!!! Неверно был совершён ввод'
            break
    return amount

print('Количество цифр в числе: ' + str(numb_of_dig(input('Введите число для подсчёта цифр в нём (без пробелов и других символов): '))))