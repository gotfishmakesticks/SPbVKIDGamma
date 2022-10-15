def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 'Треугольник по заданным сторонам существует'
    else:
        return 'Треугольника по заданным сторонам не существует'

first, second, third = int(input('Введите первую сторону треугольника: ')), int(input('Введите вторую сторону треугольника: ')), int(input('Введите третью сторону треугольника: '))
print(triangle(first, second, third))