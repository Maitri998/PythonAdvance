# 6. Check if number is prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 7. Print even numbers from list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n)

# user input
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]  # integers

print("Even numbers from the list:")
for n in numbers:
    if n % 2 == 0:
        print(n)


# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# User input and output
num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")


# 9. Simple calculator
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print("Result:", add(x, y))
elif operation == '-':
    print("Result:", subtract(x, y))
elif operation == '*':
    print("Result:", multiply(x, y))
elif operation == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operation")

# 10. Count vowels in string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

