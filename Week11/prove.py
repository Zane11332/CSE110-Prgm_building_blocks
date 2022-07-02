life_e_max = 0
life_e_min = 9999
total_life = 0
average = 0
total_life = 0
print()
with open(".\Week11\life-expectancy.csv") as life_expectancy_file:
    lines = life_expectancy_file.read().split("\n")
year_entered = int(input("Enter the year of interest: "))
print()
num_year = 0
for line in lines:
    # line_strip = line.strip()
    values = line.split(",")
    year = int(values[2])
    # if year != year_entered: // trying to work ahead so this is for dealing with year when we get to it
        # continue
    num_year += 1
    entity = values[0]
    code = values[1]
    life_expectancy = float(values[3])
    life_e_max = max(life_e_max, life_expectancy)
    life_e_min = min(life_e_min, life_expectancy)
    total_life += life_expectancy

average = total_life / num_year   
print(f"The overall max life expectancy is: {life_e_max} from {0} in {0}")
print(f"The overall min life expectancy is: {life_e_min} from {0} in {0}")
print()
print(f"For the year {year_entered}:")
print(f"The average life expectancy across all countries was {average}")
print(f"The max life expectancy was in {0} with {0}")
print(f"The min life expectancy was in {0} with {0}")
print()