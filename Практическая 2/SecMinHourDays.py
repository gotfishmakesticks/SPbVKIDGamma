def secs(fir):
    return fir * 60

def smh(fir):
    return fir / 60

def days(fir):
    return fir / 24

def indays(fir):
    return fir * 24

num1 = input("Из:\n1 - Секунд\n2 - Минут\n3 - Часов\n4 - Дней\n")

if ((int(num1) > 4) or (int(num1) < 0)):
    print("Не верный ввод")
    quit()

num2 = input("В:\n1 - Секунды\n2 - Минуты\n3 - Часы\n4 - Дни\n")

if ((int(num2) > 4) or (int(num2) < 0)):
    print("Не верный ввод")
    quit()

if (num1 == "1" and  num2 == "2") or (num1 == "2" and num2 == "3"): #Sec to Min, Min to Hour
    print(smh(int(input("Введите число: "))))

elif (num1 == "2" and  num2 == "1") or (num1 == "3" and num2 == "2"): #Min to Sec, Hour to Min
    print(secs(int(input("Введите число: "))))

elif (num1 == "1" and num2 == "3"):
    print(smh(smh(int(input("Введите число: "))))) #Sec to Hour

elif (num1 == "3" and num2 == "1"):
    print(secs(secs(int(input("Введите число: "))))) #Hour to Sec

elif (num1 == "1" and num2 == "4"):
    print(smh(smh(days(int(input("Введите число: ")))))) #Sec to Days

elif (num1 == "4" and num2 == "1"):
    print(secs(secs(indays(int(input("Введите число: ")))))) #Days to Sec

elif (num1 == "2" and num2 == "4"):
    print(smh(days(int(input("Введите число: "))))) #Min to Days

elif (num1 == "4" and num2 == "2"):
    print(secs(indays(int(input("Введите число: "))))) #Days to Min

elif (num1 == "3" and num2 == "4"):
    print(days(int(input("Введите число: ")))) #Hour to Days

elif (num1 == "4" and num2 == "3"):
    print(indays(int(input("Введите число: ")))) #Days to Hour