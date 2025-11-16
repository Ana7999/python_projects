pages = int(input())
pages_for_one_hour = int(input())
days = int(input())

total_time = pages / pages_for_one_hour

result = total_time // days
print(result)