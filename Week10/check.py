shoping_cart = []
choice = ""
enter_list = True
print()
print(f"Please enter the items of the shopping list (type: quit to finish):")
while enter_list == True:
    choice = input(f"Item: ").lower()
    if choice == "quit":
        print(f"The shopping list is:")
        for stuff in shoping_cart:
            print(f"{stuff}")

        print(f"The shopping list with indexes is:")
        for i in range(len(shoping_cart)):
            stuff = shoping_cart[i]
            print(f"{i}. {stuff}")

        index = int(input("Which item would you like to change? "))
        item = input("What is the new item? ")
        shoping_cart[index] = item

        print(f"The shopping list with indexes is:")
        for i in range(len(shoping_cart)):
            print(f"{i}. {shoping_cart[i]}")

        enter_list = False
    else:
        shoping_cart.append(choice)