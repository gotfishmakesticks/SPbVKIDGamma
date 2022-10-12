def minimum(a, b, c):
    x = a
    if b < x:
        x = b
    if c < x:
        x = c
    return x


s = []
for i in range(3):
    s.append(int(input("Введите " + str(i+1) + " число: ")))
print("Минимальное число: " + str(minimum(s[0], s[1], s[2])))
