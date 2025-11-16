deposit = input() # podatak tipa string
balance = 0.0

while deposit != "NoMoreMoney":
    current_deposit = float(deposit)
    if current_deposit < 0:
        print(" Invalid operation!")
        break
    else:
        print(f"Increase: {current_deposit:.2f}")
        balance += current_deposit
    deposit = input()
print(f"Total: {balance:.2f}")

