# Write a Python program to perform addition and multiplication with an integer, a float,
# and a complex number. Print the results and their types

str_int =int(input("Enter the integer num : ")) 
str_float = float(input("Enter the float num : ")) 
str_complex = complex(input("Enter the complex num : "))


add_int_float = str_int + str_float 
add_int_complex = str_int + str_complex
add_float_complex = str_float + str_complex

print(type(add_int_float))
print(type(add_int_complex))
print(type(add_float_complex))




