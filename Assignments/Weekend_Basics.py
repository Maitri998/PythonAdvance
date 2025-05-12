# 1. Print 'Hello, World!'
print("Hello, World!")

# 2. Take user input and print it
user_input = input("Enter something: ")
print("You entered:", user_input)

# 3. Sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# 4. Calculate area of a circle
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area of circle:", area)

# 5. Swap two variables
a = input("Enter first value (a): ")
b = input("Enter second value (b): ")
print("Before swap: a =", a, "b =", b)
a, b = b, a
print("After swap: a =", a, "b =", b)
