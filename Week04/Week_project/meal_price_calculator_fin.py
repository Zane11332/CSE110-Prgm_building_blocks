print()
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_child = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
sales_tax_input = float(input("What is the sales tax rate? "))
subtotal = (num_child * child_meal) + (num_adult * adult_meal)
sales_tax_calc = (subtotal * sales_tax_input) / 100
final_total = subtotal + sales_tax_calc
print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax_calc:.2f}")
print(f"Total: ${final_total:.2f}")
print()
pay_amount = float(input("What is the payment amount? "))
change = pay_amount  - final_total
print(f"Change: ${change:.2f}")
print()

# added stuff
# tip calculator
ten_percent = subtotal * .10
fifteen_percent = subtotal * .15
eightteen_percent = subtotal * .18
print(f"Recomended tip amount(befor tax):")
print(f"10% tip: ${ten_percent:.2f}")
print(f"15% tip: ${fifteen_percent:.2f}")
print(f"18% tip: ${eightteen_percent:.2f}")