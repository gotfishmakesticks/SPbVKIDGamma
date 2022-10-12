print("Enter an ending point\n")
x = int(input())
def sum(x):
    s = 0
    for i in range(x+1):
        s += i
    return s
print("\nSum of "+str(x)+" and N = "+str(sum(x)))