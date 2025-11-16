a = int(input())
b = int(input())

for num in range(a, b + 1):
    number = str(num)
    evan_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number):
        if index % 2 == 1:
            odd_sum += int(digit)
        elif index % 2 == 0:
            evan_sum += int(digit)

    if evan_sum == odd_sum:
        print(f"{number} ", end="")

