deposit = float(input())
months = int(input())
rate = float(input())

total_rate = deposit * rate / 100
rate_month = total_rate / 12
result = deposit + rate_month * months

print(result)
