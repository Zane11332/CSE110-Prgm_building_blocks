import math

print()
square_length = input("What is the length of a side of the square? ")
square_lenght_int = float(square_length)
print(f"The area of the square is: {square_lenght_int ** 2}")

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of rectangle? "))
print(f"The area of the rectangle is: {rectangle_length * rectangle_width}")

circle_radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is: {math.pi * circle_radius ** 2 }")
print()


square_length = input("What is the length of a side of the square? ")