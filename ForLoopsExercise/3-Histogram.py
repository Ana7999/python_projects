n = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for i in range (1, n + 1):
    num = int(input())
    if num < 200:
        p1_counter += 1
    elif 200 <= num <= 399:
        p2_counter += 1
    elif 399 <= num <= 599:
        p3_counter += 1
    elif 599 <= num <= 799:
        p4_counter += 1
    else:
        p5_counter += 1

p1_percentage = p1_counter/ n * 100
p2_percentage = p2_counter/ n * 100
p3_percentage = p3_counter/ n * 100
p4_percentage = p4_counter/ n * 100
p5_percentage = p5_counter/ n * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")