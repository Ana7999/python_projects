trip_price = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
tracks = int(input())

price = puzzle * 2.6 + dolls * 3 + bears *4.10 + minions * 8.20 + tracks * 2
toys_number = puzzle + dolls + bears + minions + tracks

if toys_number >= 50:
    price = (price - price * 0.25)

final_price = price - price * 0.1
remaining_money =  final_price - trip_price
needed_money = trip_price - final_price

if trip_price <= final_price:
    print(f"Yes! {(remaining_money):.2f} USD left.")
else:
    print(f"Not enough money! {(needed_money):.2f} USD needed.")