# This program will compute the average quiz grade for 5 students

# Set list with 5 student names Daphne, Ellie, Max, Levi and Lucas
student_names = ["Daphne", "Ellie", "Max", "Levi", "Lucas"]

# Set empty grades_list
grades_list = []

# For each student in the list prompt by name for a quiz grade
for name in student_names:
    grade_input = int(input(f"Please enter {name}'s quiz grade: "))
    grades_list.append(grade_input)

# Set grade_sum to 0 Set grade_max to none
# Compute the class quiz average
# Determine highest grade
grade_sum = 0
grade_max = None
for grade in grades_list:
    grade_sum = grade + grade_sum
    if grade_max is None or grade > grade_max:
        grade_max = grade

# Compute the average quiz score
grade_avg = grade_sum / 5

# Write the average five grades and the highest grade
print(f"""
The class's average quiz grade is: {grade_avg}
The highest quiz grade is: {grade_max}
""")

