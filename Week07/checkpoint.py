print()
num = 0
num = int(input("Please type a positive number: "))

while num < 0:
    print("Sorry, that is a negative number. Please try again.")
    num = int(input("Please type a positive number: "))

print(f"The number is: {num}") 
print()

print()
candy = ""
candy = input("May I have a piece of candy? ").lower()
while candy != "yes":
    candy = input("May I have a piece of candy? ").lower()

print("Thank you.")