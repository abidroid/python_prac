num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = num1

for i in range(2, num2 + 1):
    product += num1

print(f"Product of {num1} and {num2} is {product}")