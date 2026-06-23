students = [
    {"name": "Ansh", "gpa": 9.8},
    {"name": "Anant", "gpa": 7.8},
    {"name": "Amit", "gpa": 6.7},
]

sorted_students = sorted(students, key=lambda student: student['gpa'], reverse=True)

print("Top 3 Students:")
for student in sorted_students[:3]:
    print(f"{student['name']}: {student['gpa']}")