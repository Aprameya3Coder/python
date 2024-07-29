def add (a,b) : 
    return a+b
def subtract (a,b) :
    return a-b
def multiply (a,b) :
    return a*b
def divide (a,b) :
    return a/b if b !=0 else "Cannot divide by zero"
def default_case (a,b) :
    return "Invalid operation"
def calculator(a,b, operation) : 
    switch = {
        "add" : add,
        "subtract" : subtract,
        "multiply" : multiply,
        "division" : divide,
    }
    return switch.get(operation,default_case)(a,b)

#Example usage
num1 = 15
num2 = 5

operation = "add"
result = calculator(num1,num2,operation)
print(f"Result of {operation} : {result}:")

operation = "subtract"
result = calculator(num1,num2,operation)
print(f"Result of {operation} : {result}:")

operation = "multiply"
result = calculator(num1,num2,operation)
print(f"Result of {operation} : {result}:")

operation = "division"
result = calculator(num1,num2,operation)
print(f"Result of {operation} : {result}")

operatiion = "modulus"
result = calculator(num1,num2,operation)
print(f"Result of {operation} : {result}")



    