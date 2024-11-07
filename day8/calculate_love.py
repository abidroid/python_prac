def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    print(combined_name)

    first_count = 0
    second_count = 0

    if "T" in combined_name.upper():
        first_count += combined_name.upper().count("T")

    if "R" in combined_name.upper():
        first_count += combined_name.upper().count("R")

    if "U" in combined_name.upper():
        first_count += combined_name.upper().count("U")

    if "E" in combined_name.upper():
        first_count += combined_name.upper().count("E")

    print(f"First Count: {first_count}")

    if "L" in combined_name.upper():
        second_count += combined_name.upper().count("L")

    if "O" in combined_name.upper():
        second_count += combined_name.upper().count("O")

    if "V" in combined_name.upper():
        second_count += combined_name.upper().count("V")

    if "E" in combined_name.upper():
        second_count += combined_name.upper().count("E")

    print(f"Second Count: {second_count}")

    final_score = f"{first_count}{second_count}"
    print(final_score)


male_name = input("Enter male name: ")
female_name = input("Enter female name: ")

calculate_love_score(male_name, female_name)
