players_jersey = {}

student = {
    "name": "Ali",
    "uni": "KIU",
    "age": 21,
    "grade": "A"
}

# Access using the key
print(student["name"])  # Output: Alice

# Access using .get() (returns None if key does not exist)
print(student.get("age"))  # Output: 21
print(student.get("major"))  # Output: None

# Adding a new key-value pair
student["major"] = "Computer Science"
print(student)

# Updating an existing key's value
student["grade"] = "A+"
print(student)

# REMOVING ENTRIES
# Using del
del student["grade"]
print(student)

age = student.pop("age")
print(age)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

# Loop over dictionary
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
