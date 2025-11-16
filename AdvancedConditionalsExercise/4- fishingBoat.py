budget = int(input())
season = input().lower()
num = int(input())

price = 0.00

if season =="spring":
    price = 3000
elif season =="winter":
    price = 2600
else :
    price = 4200

if num <= 6:
    price = price * 0.90
elif  7 <= num <= 11:
    price = price * 0.85
else:
    price = price * 0.75

if season != "autumn" and num % 2 == 0:
    price = price * 0.95

if price <= budget:
    print(f"Yes! You have {(budget - price):.2f} USD left.")
else:
    print(f"Not enough money! You need {(price - budget):.2f} USD.")




