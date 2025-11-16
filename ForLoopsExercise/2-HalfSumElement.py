import sys
n = int(input())

max_number = -sys.maxsize
sum_number = 0

for i in range (1,n + 1):
    a = int(input())
    sum_number += a
    if a > max_number:
        max_number = a


sum_number = sum_number - max_number


if max_number == sum_number:
        print("Yes")
        print(f"Sum = {sum_number}")
else:
        print("No")
        print(f"Diff = {abs(max_number - sum_number)}")


