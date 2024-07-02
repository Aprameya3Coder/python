# # Write a program that takes a person's age and prints whether they are an "Adult"
# #(age 18 or older) or a "Minor" (under 18).


# age = int(input())
# if age > 18 :
#     print("Adult")
# elif age < 18 :
#     print("Minor")
# # else :
#     # print("Adult")

age = float(input())
if age >= 18 and age <= 110:  
    print("Adult")
elif age < 0 or age > 110:
    print("invalid entry")
else : 
    print("Minor")

