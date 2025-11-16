actor = input()
academy_points = float(input())
ratings = int(input())

score = academy_points

for i in range(1, ratings + 1):
    name = input()
    name_score = float(input())
    score_from_name = len(name)
    end_score = (name_score * score_from_name) / 2
    score += end_score
    if score > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {score}!")
        break
if score <= 1250.5:
    needed_points = 1250.5 - score
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")