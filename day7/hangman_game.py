import random

word_list = ["apple", "banana", "cherry", "table", "fruit", "bed", "peshawar"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a letter: ").lower()