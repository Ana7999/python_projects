
import math

record = float(input())
distance = float(input())
time = float(input())
distance_to_swim = distance * time
delay = math.floor((distance/15)) * 12.5

total_time = distance_to_swim + delay





if record > total_time :
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")