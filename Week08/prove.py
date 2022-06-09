import random


secret_word = ["red", "blue", "green", "yellow"]
guess = ""
count = 0

random_secret_word = random.choice(secret_word)
print(f"random_secret_word: ", random_secret_word)

length_word = len(random_secret_word)



for i, letter in enumerate(random_secret_word):
    print(f"The letter {letter} is at position {i}")

print()
print("Welcome to the word guessing game!\n")
print(f"Your hint is: ") #add hint stuff here
guess = input("What is your guess? ").lower()
if guess != random_secret_word:
    while guess != random_secret_word:
        print("Your guess was not correct.")
        guess = input("What is your guess? ").lower()
        count = count + 1


count = count + 1
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")
