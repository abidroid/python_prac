n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))

try:
    result = n1 / n2
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print(result)

