num = int(input("Enter number: "))

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()  
