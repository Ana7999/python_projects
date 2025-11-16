poor_marks = int(input())
current_task_name = ""
current_marks = 0
total_score = 0
score_sucs_counter = 0
score_poor_counter = 0
last_task_name = ""

while current_task_name != "Enough" or poor_marks != score_poor_counter:
    current_task_name = input()
    if current_task_name == "Enough":
        print(f"Average score: {total_score/score_sucs_counter:.2f}")
        print(f"Number of problems: {score_sucs_counter}")
        print(f"Last problem: {last_task_name}")
        break
    current_marks = int(input())
    if current_marks <= 4:
        score_poor_counter += 1
    if poor_marks == score_poor_counter:
        print(f"You need a break, {score_poor_counter} poor grades.")
        break
    last_task_name = current_task_name
    total_score += current_marks
    score_sucs_counter += 1