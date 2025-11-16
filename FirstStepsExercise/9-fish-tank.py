length = int(input())
width = int(input())
height = int(input())

percentage = float(input())

total_area_cm3 = length * width * height
total_area_l = total_area_cm3 / 1000

result = total_area_l - (total_area_l * percentage / 100)

print(result)