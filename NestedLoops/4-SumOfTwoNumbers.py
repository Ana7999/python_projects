num1 = int(input())
num2 = int(input())
magic_number = int(input())

counter = 0
flag = False


for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        counter += 1
        if i + j == magic_number:
            flag = True
            break
    if flag:
        break
if flag:
    print(f"Combination N:{counter} ({i} + {j} = {magic_number})")

else:
    print(f"{counter} combinations - neither equals {magic_number}")


