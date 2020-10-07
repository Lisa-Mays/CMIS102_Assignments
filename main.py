# Write welcome message
print("""
Welcome to the weather temperature program!
This program accepts temperature inputs in
Celsius and converts them to Fahrenheit.
It will then list the number of cool, warm,
and hot days experienced over the last 10 days.
""")

# Set array with ordinal terminology
ordinal_prompts = [
    'first', 'second', 'third', 'fourth',
    'fifth', 'sixth', 'seventh', 'eighth',
    'ninth', 'tenth'
    ]

# Set fahrenheit_temps to empty
fahrenheit_temps = []

# Set cool_day to 45 degrees fahrenheit
cool_day = 49

# Set cool_day_count to 0
cool_day_count = 0

# Set warm_day_count to 0
warm_day_count = 0

# Set hot_day to 80 degrees fahrenheit
hot_day = 80

# Set hot_day_count to 0
hot_day_count = 0


# Function to Prompt for celsius temperatures over 10 days
def ask_for_temps(prompts):
    # Set max_temps to 10
    max_temps = 10
    # Set input_celsius_temps to empty
    input_celsius_temps = []
    # While the length of input_celsius temps is less than max_temps Prompt for a temperature
    while len(input_celsius_temps) < max_temps:
        # Set the cur_prompt to the matching ordinal value
        cur_prompt = prompts[len(input_celsius_temps)]
        # Prompt for the temperature
        input_temp = input(f"Please enter your {cur_prompt} temperature: ")
        # Append the input temperature to the input_celsius_temps array
        input_celsius_temps.append(input_temp)
    return input_celsius_temps
# End Function


# Main Program

# Call celsius_temps function and pass in ordinal_prompts array
celsius_temps = ask_for_temps(ordinal_prompts)

#  Write celsius temps the user entered
print("You input the following celsius temperatures: ")
print(celsius_temps)

# Compute each temp in celsius_temps array to Fahrenheit
for temp in celsius_temps:
    fahrenheit_temps.append((float(temp) * 1.8) + 32)

# Write converted fahrenheit temperatures
print("Your temperatures converted to Fahrenheit are:")
print(["{:0.1f}".format(not_rounded) for not_rounded in fahrenheit_temps])

# Compute number of cool, warm, and hot days
for temp in fahrenheit_temps:
    # If temp is less than or equal to cool_day add 1 to the cool_day_count
    if temp <= cool_day:
        cool_day_count = cool_day_count + 1
    # If temp is greater than or equal to hot_day add 1 to the hot_day_count
    elif temp >= hot_day:
        hot_day_count = hot_day_count + 1
    # If temp isn't a hot_day or a cold_day add 1 to the hot_day_count
    else:
        warm_day_count = warm_day_count + 1

# Write the number of cool, warm, and hot days
print(f"""
The number of cool days is: {cool_day_count}
The number of warm days is: {warm_day_count}
The number of hot days is: {hot_day_count}
""")

# End Program
