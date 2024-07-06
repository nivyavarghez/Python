# 1.8. Write a function to find the factorial of a number but also store the factorials
# calculated in a dictionary.

factorial_cache = {}

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    if n in factorial_cache:
        return factorial_cache[n]
    result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")
print("Factorials stored in cache:", factorial_cache)
