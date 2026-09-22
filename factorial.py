def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
