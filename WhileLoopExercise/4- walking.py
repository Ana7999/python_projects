steps_input = input() # ostavljen input zato sto prva komanda moze da bude i going home
steps = 0
additional_steps = 0 # koraci posle Going home komande

while steps <= 10000:

    if steps_input != "Going home":
        steps += int(steps_input)

    if steps_input == "Going home":
        additional_steps = int(input())
        steps += additional_steps

        if steps > 10000:
            print(f"Goal reached! Good job!\n{steps - 10000} steps over the goal!")
            break
        else:
            print(f"{10000 - steps} more steps to reach goal.")
            break

    if steps >=10000:
        print(f"Goal reached! Good job!\n{steps - 10000} steps over the goal!")
        break
    steps_input = input()