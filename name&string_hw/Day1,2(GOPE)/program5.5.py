# Amit wants to divide two numbers in Python. Help him write a Python
# program that takes two numbers as input and prints their division result. Ensure that the
# program handles division by zero gracefully

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
if num2 == 0:
    print("Division by 0 is not allowed.")
else :
    result = num1/num2
    print("Result :", result)


