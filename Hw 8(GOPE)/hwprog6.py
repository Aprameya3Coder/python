principle_amount = int(input("Enter the principle amount : "))
rate_of_interest =float(input("Enter the rate of interest : "))
time = int(input("Enter the time : "))

simple_interest = (principle_amount*rate_of_interest*time)/100

print(f"the simple interest is {simple_interest}")