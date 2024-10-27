import random

count = 1

while count <= 4:
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    correct_answer = num1 * num2

    user_answer = int(input(f"{num1} x {num2} = "))
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect!")
        print("Correct answer:", correct_answer)

    count += 1