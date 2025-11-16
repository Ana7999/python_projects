n = int(input())

for i in range (1, n + 1):
    is_special = False
    n_string = str(i)
    sum_digits = 0

    for ch in n_string:
        sum_digits += int(ch)

    if sum_digits == 5 or sum_digits ==7 or sum_digits ==11:
        is_special = True

    print(f"{i} -> {is_special}")