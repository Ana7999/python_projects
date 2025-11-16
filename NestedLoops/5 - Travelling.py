destination = input()
minimal_budget = float(input())
money_saved = 0

while not destination == "End":

    while money_saved < minimal_budget:
        current_money = float(input())
        money_saved += current_money
    print(f"Going to {destination}!")
    destination = input()

