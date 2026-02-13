print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people_sum = int(input("How many people to split the bill? "))

tip_sum = total_bill * tip / 100
should_pay = ((total_bill + tip_sum) / people_sum)

print(f"Each person should pay: ${round(should_pay, 2)}")