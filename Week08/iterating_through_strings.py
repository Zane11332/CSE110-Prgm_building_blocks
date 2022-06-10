word = "commitment"
print()
fav_letter = input("What is your favorite letter? ").lower()

for letter in word:
    if letter == fav_letter:
        print(f"{letter.capitalize()}", end="")
    elif letter != fav_letter:
        print(f"_", end="")
fav_letter = input("What is your favorite letter? ").lower()