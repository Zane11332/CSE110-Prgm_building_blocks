import random

secret_word = ["red", "blue"]
guess = ""
count = 0
length = 0
print()
random_secret_word = random.choice(secret_word).lower()
# print(f"random_secret_word: ", random_secret_word) # uncomment this on to see random word
print()
print("Welcome to the word guessing game!\n")

print(f"Your hint is: ", end="")
length_secret_word = len(random_secret_word)
while length < length_secret_word:
    print(f"_", end=" ")
    length = length + 1
while True:
    guess = input("\nWhat is your guess? ").lower()
    count += 1
    if guess == random_secret_word:
        break
    print(f"Your hint is: ", end="")
    for j, letter in enumerate(guess):
        while letter in guess:
            for i, secret_word_letters in enumerate(random_secret_word):
                if letter == secret_word_letters:
                    if i == j:
                        print(f"{letter.capitalize()} ", end="")
                        break
                    print(f"{letter} ", end="")
                    break
            if letter != secret_word_letters:
                print(f"_ ", end="")
                break
            break  
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")
print()