groups = int(input())


total_num_of_people = 0

Makalu_counter = 0
Mont_Blanc_counter = 0
Kilimanjaro_counter = 0
K2_counter = 0
Everest_counter = 0

for i in range(1, groups + 1):
        num_of_people = int(input())
        total_num_of_people += num_of_people
        if num_of_people <= 5:
            Makalu_counter += num_of_people


        elif 6 <= num_of_people <= 12:
            Mont_Blanc_counter += num_of_people


        elif 13 <= num_of_people <= 25:
            Kilimanjaro_counter += num_of_people
        elif 26 <= num_of_people <= 40:
            K2_counter += num_of_people

        elif num_of_people > 40:
            Everest_counter += num_of_people

Makalu_percentage = Makalu_counter / total_num_of_people * 100
Mont_Blanc_percentage = Mont_Blanc_counter / total_num_of_people * 100
Kilimanjaro_percentage = Kilimanjaro_counter / total_num_of_people * 100
K2_percentage = K2_counter / total_num_of_people * 100
Everest_percentage = Everest_counter / total_num_of_people * 100

print(f"{Makalu_percentage:.2f}%")
print(f"{Mont_Blanc_percentage:.2f}%")
print(f"{Kilimanjaro_percentage:.2f}%")
print(f"{K2_percentage:.2f}%")
print(f"{Everest_percentage:.2f}%")