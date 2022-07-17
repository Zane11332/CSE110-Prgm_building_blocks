def convert_temp(value):
        num = (value * 9/5) + 32
        return num
def windchill_calc(T, mph):
    a_number = 35.74 + 0.6215 * T - 35.75 * (mph ** 0.16) + 0.4275 * T * (mph ** 0.16)
    return a_number

number = 0
mph = 5
windchill = 0
temp = 0

value = int(input(f"What is the temperature? "))
f_c = input(f"Fahrenheit or Celsius (F/C)? ").lower()
if f_c == "c":
    value = convert_temp(value)

while mph <= 60:
    windchill = windchill_calc(value, mph)
    print(f"At temperature {value:.1f}F, and wind speed {mph} mph, the windchill is: {windchill:.2f}F")
    mph += 5

