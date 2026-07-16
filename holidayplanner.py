print("====================================")
print("    Welcome to HOLIDAY PLANNER      ")
print("====================================")
choice = int(input("Do you want to go to the beach(1) or the mountains(2)"))
if choice == 1:
    choice = int(input("Do you want to build sandcastles(1) or swim(2)"))
    if choice == 1:
        print("You picked sandcastle building")
        print("Best time: Evening")
        print("Bring: Bucket and spade")
    elif choice == 2:
        print("You picked swimming")
        print("Best time: Afternoon")
        print("Bring: Extra clothing and swim suit")
    else:
        print("Invalid choice, only use 1 or 2")
elif choice == 2:
    choice = int(input("Do you want to go hiking(1) or camping(2)"))
    if choice == 1:
        print("You picked hiking")
        print("Best time: Morning")
        print("Bring: Hiking shoes, water bottle, Daypack")
    elif choice == 2:
        print("You picked camping")
        print("Best time: Afternoon")
        print("Bring: Tent, sleeping bag, normal neccesities(water, food, etc.)")
    else:
        print("Invalid choice, please enter only 1 or 2")
else:
    print("Invalid choice, please enter only 1 or 2")
        
