num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
message = """
Select Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Your choice: ? """

choice = input(message)

if choice == "1":
    print(num1 + num2)
elif choice == "2":
    print(num1 - num2)
elif choice == "3":
    print(num1 * num2)
elif choice == "4":
    print(num1 / num2)
else:
    print("Invalid input")