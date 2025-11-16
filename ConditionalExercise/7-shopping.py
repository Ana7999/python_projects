budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memories = int(input())

video_cards_cost = video_cards * 250
processors_costs = processors * (video_cards_cost * 0.35)
ram_memories_costs = ram_memories * video_cards_cost * 0.1
all_costs = video_cards_cost + processors_costs + ram_memories_costs

if video_cards > processors:
    all_costs-= all_costs * 0.15

money_left = abs(budget - all_costs)

if all_costs <= budget:
    print(f"You have {money_left:.2f} USD left!")

else:
    print(f"Not enough money! You need {money_left} USD more!")