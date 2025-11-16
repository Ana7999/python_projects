chicken_number = int(input())
fish_number = int(input())
vege_number = int(input())

chicken_price = chicken_number * 10.35
fish_price = fish_number * 12.40
vege_price = vege_number * 8.15
total_price = chicken_price + fish_price + vege_price

dessert_price = total_price * 20/100

delivery_price = 2.50

results = total_price + dessert_price + delivery_price

print(results)

