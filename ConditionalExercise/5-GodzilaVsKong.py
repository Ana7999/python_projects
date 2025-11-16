budget = float(input())
extras = int(input())
clothes_per_extras = float(input())

clothes_total = extras * clothes_per_extras
decor = budget * 0.1

if extras > 150:
    clothes_total = clothes_total - clothes_total * 0.1

total_costs=  clothes_total +  decor
total= total_costs - budget
total1= budget - total_costs

if total_costs>budget:
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} USD more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {total1:.2f} USD left.")







