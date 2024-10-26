import random

dice_rolls = []
count = 0

one = 0; two =0; three = 0; four = 0; five = 0; six = 0

for count in range(0,6000):
    random_num = random.randint(1,6)
    dice_rolls.append(random_num)
    if random_num == 1:
        one = one+1
    elif random_num == 2:
        two = two+1
    elif random_num == 3:
        three = three+1
    elif random_num == 4:
        four = four+1
    elif random_num == 5:
        five = five+1
    else:
        six = six+1

print(f"One appeared {one} times")
print(f"Two appeared {two} times")
print(f"Three appeared {three} times")
print(f"Four appeared {four} times")
print(f"Five appeared {five} times")
print(f"Six appeared {six} times")

