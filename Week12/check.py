oldest = 99
name = ""
people = [
    "Stephanie 36",
    "Michael 2",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Jacob 10"
    ]
for person in people:
    parts = person.split()
    person_name = parts[0]
    person_age = int(parts[1])

    if person_age < oldest:
        oldest = person_age
        name = person_name

print(f"The youngest age is: {oldest}")
print(f"The youngest persons name is: {name}")