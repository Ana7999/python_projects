

type_of_projection = input()
columns = int(input())
rows = int(input())


cinema_capacity = columns * rows
income = 0

if type_of_projection == "Premiere":
    income = cinema_capacity * 12
elif type_of_projection == "Normal":
    income = cinema_capacity * 7.5
elif type_of_projection == "Discount":
    income = cinema_capacity * 5

print(f"{income:.2f} USD")


