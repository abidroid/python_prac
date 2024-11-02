

def table():
    for i in range(1, 11):
        print(6, " X ", i, " = ", 6*i)


def greet_user(user):
    print(f"Welcome {user}")

def sum_of_two_nums(a, b):
    print(f"The sum of {a} and {b} is {a+b}")

def square(num):
    return num*num

def is_even( num ):
    if num % 2 == 0:
        return True
    else:
        return False


def factorial(num):
    factorial_of_num = 1
    for i in range(2, num+1):
        factorial_of_num *= i
    return factorial_of_num

def product_without_asterisk(num1, num2):
    product = num1
    count = 2
    while count <= num2:
        product += num1
        count += 1
    print(product)



product_without_asterisk(4,5)

# for i in range( 1, 11):
#     print(f"{i}! = {factorial(i)}")


#print(is_even(5))



# print(f"Square of 10 is {square(10)}")
# sum_of_two_nums(3, 5)
#greet_user("Ali")
#table()