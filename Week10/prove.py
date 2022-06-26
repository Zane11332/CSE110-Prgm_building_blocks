shoping_cart = []
prices = []
enter_list = True
total = 0
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
        item = input(f"What item would you like to add? ")
        shoping_cart.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        prices.append(price)
        print(f"'{item}' has been added to the cart. \n")
    elif choice == "2":
        print(f"The contents of the shopping cart are:")
        for i in range(len(shoping_cart)):
            print(f"{i + 1}. {shoping_cart[i]} - ${prices[i]:.2f}")
    elif choice == "3":
        index = int(input(f"Which item would you like to remove? "))
        shoping_cart.pop(index - 1)
        prices.pop(index - 1)
        print(f"Item removed.")
    elif choice == "4":
        for i in range(len(prices)):
            total += prices[i]
        print(f"The total price of the items in the shopping cart is ${total}")

    elif choice == "5":
        print(f"Thank you. Goodbye.")
        enter_list = False
    else:
        print(f"invalid response please select again. ")
