type_of_flowers = input()
num = int(input())
budget = int (input())

price = 0.00

if type_of_flowers =="Roses":
    price = num * 5
    if num > 80:
        price = price * 0.90

elif type_of_flowers =="Dahlias":
    price = num * 3.8
    if num > 90:
        price = price * 0.85

elif type_of_flowers =="Tulips":
    price = num * 2.80
    if num > 80:
        price = price * 0.85

elif type_of_flowers =="Narcissus":
    price = num * 3
    if num < 120:
        price = price * 1.15

elif type_of_flowers =="Gladiolus":
    price = num * 2.50
    if num < 80:
        price = price * 1.20

if price <= budget:
    print(f"Hey, you have a great garden with {num} {type_of_flowers} and {(budget-price):.2f} USD left.")
else:
    print(f"Not enough money, you need {(price - budget):.2f} USD more.")