basketball_fee = int(input())
basketball_sneakers = basketball_fee - (basketball_fee * 40/100)
basketball_outfit = basketball_sneakers - (basketball_sneakers * 0.2)
ball = basketball_outfit /4
basketball_accessories = ball/5

result = basketball_fee + basketball_sneakers + basketball_outfit + ball + basketball_accessories
print(result)