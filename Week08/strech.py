import math

word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
print()
number = int(input("Please enter a number: "))

for i, letter in enumerate(word):
    if letter == " ":
        count = i - 1
    if i % number == 0:
        print(f"{letter.capitalize()}", end="")
    else:
        print(f"{letter}", end="")

