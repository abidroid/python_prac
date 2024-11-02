choice = "Yes"

while choice == "Yes":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum = {num1 + num2}")
    choice = input("Would you like to try again? (Yes/No): ")

print("Thank you!")