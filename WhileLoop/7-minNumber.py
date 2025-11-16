import sys
n = input()

min_n = sys.maxsize

while n != "Stop":
    current_n = int(n)
    if current_n < min_n:
        min_n = current_n
    n = input()
print(min_n)