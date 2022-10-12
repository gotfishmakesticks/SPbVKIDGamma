print("Input an ending factorial point\n")
n = int(input())
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n
print("\nYour factorial is - "+str(factorial(n)))