tournament = int(input())
starting_points = int(input())

total_points = 0
total_wins = 0

for i in range (1, tournament + 1):
    position = input()
    if position == "W":
        total_points += 2000
        total_wins += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":
        total_points += 720

points = starting_points + total_points
print(f"Final points: {points}")

average_points = int(total_points / tournament)
print(f"Average points: {average_points}")

wins_percantage = total_wins / tournament * 100
print(f"{wins_percantage:.2f}%")






