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


print(is_even(5))



# print(f"Square of 10 is {square(10)}")
# sum_of_two_nums(3, 5)
#greet_user("Ali")
#table()