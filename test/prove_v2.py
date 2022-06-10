import random

secret_word = ["red", "blue", "green", "yellow"]
guess = ""
count = 0
length = 0
print()
random_secret_word = random.choice(secret_word).lower()
print(f"random_secret_word: ", random_secret_word)
print()
print("Welcome to the word guessing game!\n")

print(f"Your hint is: ", end="")
length_secret_word = len(random_secret_word)
while length < length_secret_word:
    print(f"_", end=" ")
    length = length + 1

guess = input("\nWhat is your guess? ").lower()

if guess != random_secret_word:
    while guess != random_secret_word:
        print(f"Your hint is: ", end="")
        for i, secret_letter in enumerate(random_secret_word):
            if guess == secret_letter:
                print(f"{guess}")
            else:
                print(f"_ ", end="")
        for letter in guess:
            if letter == secret_letter:
                print(f"{letter}")
                       
        guess = input("\nWhat is your guess? ").lower()
        count = count + 1

count = count + 1
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")
print()
