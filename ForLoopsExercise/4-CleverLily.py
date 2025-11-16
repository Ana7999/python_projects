age = int(input())
price = float(input())
toy_price = int(input())

sum = 0
#novac skupljen za rodjendane
time = 0
#po koji put dobija novac
toys = 0
#novac dobijen prodajom igracaka

for n in range (1, age + 1):
    if n % 2 ==0:
        time += 1
        sum += time * 10
# za parne novac, za neparne toys
    else:
        toys += toy_price

total = sum - time + toys

diff = abs(total - price)
if total >= price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


