budget = float(input())
season = input()

place = ""
price = 0.00
if budget <= 100:
    place = "Serbia"
    if season == "summer":
        price = budget * 0.30
    else:
        price = budget * 0.70

elif 100 < budget <= 1000:
    place = "Balkans"
    if season == "summer":
        price = budget * 0.40
    else:
        price = budget * 0.80
else:
    place = "Europe"
    price = budget * 0.90

print(f"Somewhere in {place}")

if season == "summer" and place != "Europe":
    print(f"Camp - {(price):.2f}")
else:
    print(f"Hotel - {(price):.2f}")



