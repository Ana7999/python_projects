
money_for_trip = float(input())
money_in_hand = float(input())
days_counter = 0
days_spend_counter = 0

while money_in_hand < money_for_trip and days_spend_counter < 5:
    days_counter += 1
    action_type = input()
    save_spent_money = float(input())

    if action_type == "spend":
        days_spend_counter += 1
        money_in_hand -= save_spent_money
        if money_in_hand < 0:
            money_in_hand = 0

    elif action_type == "save":
        money_in_hand += save_spent_money
        days_spend_counter = 0



    if money_in_hand >= money_for_trip:
        print(f"You saved the money for {days_counter} days.")
        break

    if days_spend_counter == 5:
        print(f"You can't save the money.\n{days_spend_counter}")
        break

