total_lapses = int(input("Enter total lapses ? "))

lapse_time_list = []

for i in range(total_lapses):
    time = int(input(f"Enter time in second for lap {i + 1} : "))
    lapse_time_list.append(time)

smallest_time = lapse_time_list[0]
largest_time = lapse_time_list[0]
average_time = 0

for time in lapse_time_list:
    average_time += time
    if time < smallest_time:
        smallest_time = time
    if time > largest_time:
        largest_time = time

average_time = average_time / len(lapse_time_list)

print("Smallest lapse time is : ", smallest_time)
print("Largest lapse time is : ", largest_time)
print("Average lapse time is : ", average_time)
