

def table(number, limit):
    for i in range(1, limit+1):
        print(f"{number} X {i} = {number*i}")


# named arguments
table(limit=10, number=5)