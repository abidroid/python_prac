
list = [ 4, 87, 34, 87, 32, 98, 7, 45, 76]

largest = list[0]

# Traversing
for number in list:
    if number > largest:
        largest = number

print("Largest number in list is ", largest)


