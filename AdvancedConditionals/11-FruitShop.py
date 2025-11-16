fruit = input().lower()
day = input().lower()
quantity = float(input())
#
price= 0

if day == "monday" or day=="tuesday" or day=="wednesday" or day =="thursday" or day =="friday":
    if fruit == "banana":
        price = 2.50
        total_cost = quantity * price
        print(f"{total_cost:.2f}")
    elif fruit == "apple":
         price = 1.20
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "orange":
         price = 0.85
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "grapefruit":
         price = 1.45
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "kiwi":
         price = 2.70
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "pineapple":
         price = 5.50
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "grapes":
         price = 3.85
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    else:
        print("error")
elif day =="saturday"  or day == "sunday":
    if fruit == "banana":
        price = 2.70
        total_cost = quantity * price
        print(f"{total_cost:.2f}")
    elif fruit == "apple":
         price = 1.25
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "orange":
         price = 0.90
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "grapefruit":
         price = 1.60
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "kiwi":
         price = 3.00
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "pineapple":
         price = 5.60
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    elif fruit == "grapes":
         price = 4.20
         total_cost = quantity * price
         print(f"{total_cost:.2f}")
    else:
         print("error")
else:
    print("error")
