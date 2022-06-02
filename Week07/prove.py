secret_word = "mosiah"
guess = ""
count = 0

print()
print("Welcome to the word guessing game!\n")
while guess != secret_word:
    guess = input("What is your guess? ").lower()
    print("Your guess was not correct.")
    count = count + 1
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")