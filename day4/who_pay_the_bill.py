import random

friends = ["Arif", "Rehmat", "Shahroon", "Jamal", "Humayun", "Rashid"]

# Generate a random float between 0.0 and 1.0
# it is done with random.random() function
random_num = int(random.random() * len(friends))

person_to_pay_bill = friends[random_num]
print(person_to_pay_bill)