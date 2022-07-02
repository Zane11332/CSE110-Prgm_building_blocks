life_e_max = 0
life_e_min = 9999
total_life = 0

with open("..\Week11\life-expectancy.csv") as life_expectancy_file:
  lines = life_expectancy_file.read().split("\n")
  year_entered = int(input("Enter the year of interest: "))
  
for line in lines:
    values = line.split(",")
    line_strip = lines.strip()
    final = line_strip.split(",")
    entity = final[0]
    code = final[1]
    year = int(final[2])
    life_expectancy = float(final[3])

    # ['Entity', 'Code', 'Year', 'Life expectancy']
    if life_e_max < life_expectancy:
        life_e_max = life_expectancy

    if life_e_min > life_expectancy:
        life_e_min = life_expectancy

    total_life += life_expectancy
    length = len(line)
    average = total_life / length

print(total_life)
print(length)
    
print(f"The overall max life expectancy is: {life_e_max}")
print(f"The overall max life expectancy is: {life_e_min}")
print(f"For the year {year_entered}:")
print(f"The average life expectancy across all countries was {average}")


