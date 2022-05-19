print()
choice_01 = input(f"You find yourself at the entrance of a cave. You can choose to ENTER the cave or LOOK around. ").lower()

if choice_01 == "enter":
    choice_01_01 = input(f"You step into the cave and it is very dark. You can almost make out a shape a little way off. Do you APPROACH or do you WAIT?").lower()
    if choice_01_01 == "approach":
        print("You die. A creature has eaten you. The End.")
    elif choice_01_01 == "wait":
        print("You wait and the figure moves off into the distance. You proceed slowly. ")
        choice_01_01_02 = input("You fumble your way around and find a small opening that seems to be blocked by a small door. Do you OPEN or LEAVE the door? ").lower()
        if choice_01_01_02 == "open":
            print("You win the game and get all the money in the room GG.")
        elif choice_01_01_02 == "leave":
            print("You leave and walk right into the big thing at the end of the cave. It eats you. YOU HAVE DIED...so sorry. ")
        else:
            print("Now you broke the whole thing and have to start over dang it.")
    else:
        print("You can't type that. Try again.")

elif choice_01 == "look":
    choice_01_02 = input(f"You look around and find that there are some unlit torches on the wall of the cave. Using your handy dandy lighter in your pocket you can LIGHT the torch or LEAVE it alone. ").lower()
    if choice_01_02 == "light":
        print("You light the torch and proceed into the cave. You see a small shiny object glint in the light of your torch. The Ring you came looking for was just right there good on you for lighting your torch. You grab the ring and get out of there. ")
    elif choice_01_02 == "leave":
        print("As you leave you hear a terrible sound from inside the cave. Good choice it sounded hungry. ")
    else:
        print("You can't type that. Try again.")

    

