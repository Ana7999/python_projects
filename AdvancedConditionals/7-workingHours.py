hour = int(input())
day = input().lower()

if hour >= 10 and hour <=18:
    if day == "monday":
        print("open")
    elif day == "tuesday":
        print("open")
    elif day == "wednesday":
        print("open")
    elif day == "thursday":
        print("open")
    elif day == "friday":
        print("open")
    elif day == "saturday":
        print("open")

if day == "sunday"  or hour <10 or hour>18:
    print("closed")