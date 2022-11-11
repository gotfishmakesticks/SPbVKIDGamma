print("Введите вес тела и нажмите Enter, затем введите рост и снова нажмите Enter: ")
weight = int( input() )
height = int( input() )
bodyMassIndex = weight / height**2
print("Индекс массы тела равен " + str(bodyMassIndex))