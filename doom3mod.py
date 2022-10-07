weird_temp = True
while weird_temp:
    positive = 0
    negative = 0
    print("Please, enter 15 any integral numbers\nIf you want to exit the program, enter 213\n")
    for i in range(15):
        temp = int(input())
        if temp > 0:
            positive+=temp                                  #c = 5, a = 2. c = c + a = 7.
        if temp < 0:
            negative+=temp
        if temp == 0:
            print("Do you consider 0 as..\n1 - Positive\n2 - Negative")
            zero = int(input())
            if zero == 1:
                positive+=temp
            if zero == 1:
                negative+=temp
        if temp == 213:
            print("Okay, do you want to add this number or close the program?\nI'm ok with both variants tho\n"
                  "1 - Add\n2 - Exit")
            inp2 = int(input())
            if inp2 == 1:
                positive+=temp
            if inp2 == 2:
                quit()
    print("\nTotal sum of positive numbers: "+str(positive)+"\nTotal sum of negative numbers: "+str(negative))
    while True:
        print("\nHey, do you want to stay?\n1 - Yes\n2 - No")
        var = int(input())
        if var == 1:
            break
        if var == 2:
            print("Okay, bye!")
            weird_temp = False
            break
        else:
            print("Yeah, bye.")
            weird_temp = False
            break



