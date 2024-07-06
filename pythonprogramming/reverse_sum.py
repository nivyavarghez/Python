def is_palindrome(num):
    return str(num) == str(num)[::-1]

def reverse_number(num):
    return int(str(num)[::-1])

def reverse_and_add_until_palindrome(num):
    steps = 0
    while not is_palindrome(num):
        reversed_num = reverse_number(num)
        num = num + reversed_num
        steps += 1
        print(f"Step {steps}: {num}")
    return num

initial_number = int(input("Enter the initial number: "))
result = reverse_and_add_until_palindrome(initial_number)
print(f"Initial number: {initial_number}")
print(f"Palindrome: {result}")
