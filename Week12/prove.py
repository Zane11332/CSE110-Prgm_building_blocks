life_e_max = 0
life_e_min = 9999
year_e_max = 0
year_e_min = 9999
total_life = 0
average = 0
name_max = ""
year_max = ""
name_min = ""
year_min = ""
year_amount = 0
print()
with open(".\Week11\life-expectancy.csv") as life_expectancy_file:
    lines = life_expectancy_file.read().split("\n")
year_entered = int(input("Enter the year of interest: "))
print()
for line in lines:
    line_strip = line.strip()
    values = line.split(",")
    year = int(values[2])
    entity = values[0]
    code = values[1]
    life_expectancy = float(values[3])
    if life_e_max < life_expectancy:
        life_e_max = life_expectancy
        name_max = entity
        year_max = year

    elif life_e_min > life_expectancy:
        life_e_min = life_expectancy
        name_min = entity
        year_min = year

    if year == year_entered:
        total_life += life_expectancy
        year_amount += 1
        if year_e_max < life_expectancy:
            year_e_max = life_expectancy
            name_max = entity
        elif year_e_min > life_expectancy:
            year_e_min = life_expectancy
            name_min = entity
average = total_life / year_amount   

print(f"The overall max life expectancy is: {life_e_max} from {name_max} in {year_max}")
print(f"The overall min life expectancy is: {life_e_min} from {name_min} in {year_min}")
print()
print(f"For the year {year_entered}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {name_max} with {year_e_max}")
print(f"The min life expectancy was in {name_min} with {year_e_min}")
print()