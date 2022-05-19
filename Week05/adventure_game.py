print()
choice_01 = input(f"You find yourself at the entrance of a cave.\
 You can choose to ENTER the cave or LOOK around. ").lower()

if choice_01 == "enter":
    choice_01_01 = input(f"You step into the cave and it is very dark.\
    You can almost makeout a shape a little way off.\
    Do you APPROACH or do you WAIT?").lower()
    if choice_01_01 == "approach":
        print("You die")
    elif choice_01_01 == "wait":
        print("You wait and the figure moves off into the distane. ")
    else:
        while True:
            choice_01_01 = input("You have to choose: APPROACH or WAIT. ").lower()
            if choice_01_01 == "approach":
                print("die")
                break
            elif choice_01_01 == "wait":
                print("ok")
                break

elif choice_01 == "look":
    input("You look around")

else:
    while True:
        choice_01 = input("You have to choose: ENTER or LOOK. ").lower()
        if choice_01 == "enter":
            choice_01_01 = input(f"You step into the cave and it is very dark.\
            You can almost make out a shape a little way off. Do you APPROACH\
            or do you WAIT?")
            break
        elif choice_01 == "look":
            break


    
