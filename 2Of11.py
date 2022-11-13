print("Введите 4 числа (после ввода каждого из чисел нажмите Enter: ")
array = []
i = 0
for i in range(4):
    array.append( int( input() ) )
if array[0] == array[1] == array[2] == array[3]:
    print("=")
else:
    print("!=")