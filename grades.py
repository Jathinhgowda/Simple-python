# Define the list of students and their grades
students_grades = [
    {"name": "Akash", "grade": 85},
    {"name": "Hitesh", "grade": 98},
    {"name": "Charan", "grade": 92},
    {"name": "Govardhan", "grade": 88},
    {"name": "Jathin", "grade": 90}
]

# Calculate the average grade
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

# Extract grades from the student data
grades = [student["grade"] for student in students_grades]

# Calculate the average grade
average_grade = calculate_average(grades)

# Write the results to a text file
with open("student_averages.txt", "w") as file:
    file.write("Student Grades:\n")
    for student in students_grades:
        file.write(f"{student['name']}: {student['grade']}\n")
    file.write(f"\nAverage Grade: {average_grade:.2f}\n")

print("Results have been written to 'student_averages.txt'")
print(f"\nAverage Grade: {average_grade:.2f}\n")
