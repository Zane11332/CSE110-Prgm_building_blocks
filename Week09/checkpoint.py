friends = []
names = ""
while names != "end":
    names = input(f"Type the name of a friend: ")
    if names == "end":
        print(f"Your friends are:")
        print(f"{friends}")
    friends.append(names)

# ----------------------------------
friends = []
name = None
while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end":
        friends.append(name)
print()
print("Your friends are:")
for friend in friends:
    print(friend)