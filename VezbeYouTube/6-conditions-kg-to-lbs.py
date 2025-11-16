

weight = float(input("weight: "))
units = input("L or K: ")

if units.upper() =="L":
    converted = weight * 0.453
    print(f"You are {converted}kg")
elif units.upper() =="K":
    converted_1 = weight * 2.2046250

    print(f"You are {converted_1} lbs")



