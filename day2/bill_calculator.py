print("Welcome to Bill Calculator!")
total_bill = int(input("What is your total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_tip = total_bill * tip_percentage / 100

total_bill = total_bill + total_tip

bill_per_person = total_bill / number_of_people

print(f"Each person should pay: ${bill_per_person:.2f}")