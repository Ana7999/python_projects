
hours = int(input())
minutes = int(input())
hours_in_minutes= hours * 60

total_minutes =  hours_in_minutes + minutes + 15

final_hours = total_minutes // 60
final_minutes = total_minutes % 60

if final_hours == 24:
    final_hours = 0

if final_minutes<10:
    print(f"{final_hours}:0{final_minutes}")
else:
    print(f"{final_hours}:{final_minutes}")