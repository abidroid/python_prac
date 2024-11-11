def calculate_grade( marks):
    if marks >= 91:
        return "Outstanding"
    elif marks >= 81:
        return "Exceeds Expectations"
    elif marks >= 71:
        return "Acceptable"
    else:
        return "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_scores.items():
    grade = calculate_grade(value)
    student_grades[key] = grade

print(student_grades)