print("Enter a number\n")
num = int(input())
num = abs(num)
def counter(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
print("\nCapacity is "+str(counter(num)))