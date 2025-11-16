students_name = input()
current_year_grade = 0
grade_counter = 0
class_year = 1
failed_year = 0
average_grade = 0

while class_year <= 12:
    current_year_grade = float(input())
    if current_year_grade >= 4:
        grade_counter += current_year_grade
        class_year += 1
    else:
        failed_year += 1
        if failed_year > 1:
            break
average_grade = grade_counter/12
if class_year == 13:
    print(f"{students_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{students_name} has been excluded at {class_year} grade")