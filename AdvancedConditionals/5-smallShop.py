product = input().lower()
town = input().lower()
quantity = float(input())

if town == "london":
    if product == "coffee":
        print(quantity * 0.5)
    elif product == "water":
        print(quantity * 0.8)
    elif product == "beer":
        print(quantity * 1.20)
    elif product == "sweets":
        print(quantity * 1.45)
    elif product == "peanuts":
        print(quantity *1.60 )

elif town == "rome":
    if product == "coffee":
        print(quantity * 0.4)
    elif product == "water":
        print(quantity * 0.7)
    elif product == "beer":
        print(quantity * 1.15)
    elif product == "sweets":
        print(quantity * 1.30)
    elif product == "peanuts":
        print(quantity * 1.50)

elif town =="paris":
        if product == "coffee":
            print(quantity * 0.45)
        elif product == "water":
            print(quantity * 0.70)
        elif product == "beer":
            print(quantity * 1.10)
        elif product == "sweets":
            print(quantity * 1.35)
        elif product == "peanuts":
            print(quantity * 1.55)





