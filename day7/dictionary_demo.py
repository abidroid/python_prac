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