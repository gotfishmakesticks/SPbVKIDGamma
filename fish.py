#возвращает ограниченное с 2 сторон значение
def clamp(val, min, max):
	if val > max:
		return max
	elif val < min:
		return min
	else:
		return val
#нужно для возвращения в меню после завершения действия
def inputer():
	a = input("Введите что угодно, чтобы продолжить...")
	return 0
#создаем целочисленное значение без ошибок
def intinput():
	a = input()
	try:
		ret = int(a)
		return ret
	except:
		if a != "":
			b = ""
			for i in range(len(a)):
				c = a[i]
				if c.isdigit():
					b = b + c
			return int(b)
		else:
			return 0
#дробное выражение без ошибок
def floatinput():
	try:
		a = input()
		ret = float(a)
		return ret
	except:
		d = False
		if a != "":
			b = ""
			for i in range(len(a)):
				c = a[i]
				if c.isdigit() or c == "." and d == False:
					b = b + c
					if c == ".":
						d = True
				elif c.isdigit():
					b = b + c
			return float(b)
		else:
			return 0
#для красоты, возвращает инфу о проекте
def about():
	name = "Got Fish? Make Python Module!"
	author = "ГФМСХЛ)"
	version = "v.1.2.0"
	print(name + " " + version + " by " + author)
#список изменений, ну так, чисто для себя)
def changelog():
	print("Список изменений:\n"
	+ "v.1.0.0 (16.11.22):\n"
	+ "- Добавлен метод clamp\n"
	+ "- Добавлен метод inputer\n"
	+ "- Добавлен метод about\n"
	+ "v.1.1.0 (16.11.22):\n"
	+ "- Добавлен метод intinput\n"
	+ "- Добавлен метод changelog\n"
	+ "v.1.2.0 (18.11.22):\n"
	+ "- Добавлен метод floatinput\n"
	+ "- Добавлены методы для работы с 2д массивами:\n"
	+ "ds_grid_create\n"
	+ "ds_grid_print\n"
	+ "ds_grid_get_column\n"
	+ "ds_grid_set_column\n"
	+ "ds_grid_get_row\n"
	+ "ds_grid_set_row")
#инструменты для работы с 2д массивами
#создает 2д массив
def ds_grid_create(width, height, value):
	ret = []
	for i in range(height):
		reti = []
		for j in range(width):
			reti.append(value)
		ret.append(reti)
	return ret
#выводит 2д массив в более понятном виде
def ds_grid_print(grid):
	for i in range(len(grid)):
		print(grid[i])
#возвращает значения в колонке
def ds_grid_get_column(grid, column):
	ret = []
	for i in range(len(grid)):
		ret.append(grid[i][column])
	return ret
#заменяет значения в колонке
def ds_grid_set_column(grid, column, value):
	for i in range(len(grid)):
		grid[i][column] = value
	return (grid)
#заменяет значения в ряду
def ds_grid_set_row(grid, row, value):
	for i in range(len(grid[row])):
		grid[row][i] = value
	return grid
#функция аналогична просто grid[row], но создана, чтобы не путаться
def ds_grid_get_row(grid, row):
	return grid[row]
#КРАСИВО вывести 2д массив, функция не закончена
def ds_grid_nice_print(grid):
	maxlen = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if len(str(grid[i][j])) > maxlen:
				maxlen = len(str(grid[i][j]))
	