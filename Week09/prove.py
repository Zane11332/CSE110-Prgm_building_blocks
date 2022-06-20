shoping_cart = []
enter_list = True
print()
print(f"Welcome to the Shopping Cart Program!")
print()
while enter_list == True:
    print(f"Please select one of the following:")
    print(f"1. Add item")
    print(f"2. View cart")
    print(f"3. Remove item")
    print(f"4. Compute total")
    print(f"5. Quit")
    choice = input(f"Please enter an action: ")

    if choice == "1":
        item = input(f"What item would you like to add? ").lower()
        shoping_cart.append(item)
        print(f"'{item}' has been added to the cart. ")
    elif choice == "2":
        for items in shoping_cart:
            print(items)
    elif choice == "3":
        print(f"Remove item")
    elif choice == "4":
        print(f"Compute total")
    elif choice == "5":
        enter_list = False
    else:
        print(f"invalid response please select again. ")
