# Aarav wants to perform some basic calculations in Python. Help
# him write a Python program that takes two numbers as input and calculates their sum,
# difference, product, and quotient. Print the results.

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 #Handle division by zero gracefully

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Division: " , quotient)



