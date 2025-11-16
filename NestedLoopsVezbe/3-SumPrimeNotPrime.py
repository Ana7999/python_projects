sum_prime = 0
sum_not_prime = 0


while True:
    is_prime = True  # pretpostavka da je boj prost
    input_num = input() # ili broj ili Stop
    if input_num == "stop":
        break
    num = int(input_num)
    if num < 0:
        print("Number is negative. ")
        continue
    elif num == 1:
        sum_not_prime += 1
        continue
    else:
        for i in range (2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        sum_prime += num
    else:
        sum_not_prime += num
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_not_prime}")
