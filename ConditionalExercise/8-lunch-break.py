import math

series = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 4
relax_time = break_duration / 8

needed_time = relax_time + lunch_time + episode_duration

rest_time = abs(break_duration - needed_time)

if needed_time <= break_duration:
    print(f"You have enough time to watch {series} and left with {math.ceil(rest_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(rest_time)} more minutes.")

