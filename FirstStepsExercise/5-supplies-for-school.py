pen = int(input())
markers = int(input())
litres = int(input())
percent = int(input())

price_pen = pen * 5.80
price_markers = markers * 7.20
price_deterdzent = litres * 1.20

total_price = price_pen + price_markers + price_deterdzent
final_price = total_price - (total_price * 25 / 100)
print(final_price)


