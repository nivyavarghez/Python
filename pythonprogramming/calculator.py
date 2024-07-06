def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select the operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    ch = input("Enter your choice (1/2/3/4): ")

    if ch in ('1', '2', '3', '4'):
        try:
            x = float(input("Enter Number 1: "))
            y = float(input("Enter Number 2: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == '1':
            print(x, "+", y, "=", add(x, y))
        elif ch == '2':
            print(x, "-", y, "=", subtract(x, y))
        elif ch == '3':
            print(x, "*", y, "=", multiply(x, y))
        elif ch == '4':
            result = divide(x, y)
            if isinstance(result, str):
                print(result)
            else:
                print(x, "/", y, "=", result)

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()

        if next_calculation != "yes":
            break
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")
