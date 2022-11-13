print("Введите вес тела (кг) и нажмите Enter, затем введите рост (см) и снова нажмите Enter: ")
weight = int( input() )
height = int( input() )
bodyMassIndex = weight / (height/100)**2
print("Индекс массы тела равен " + str(bodyMassIndex))
