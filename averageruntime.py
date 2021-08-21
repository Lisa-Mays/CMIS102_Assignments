# This program will calculate the average run time of 1 mile races

# Print welcome
print("""
Welcome to the 1 mile race time calculator
This program will calculate your average time
for as many 1 mile races as you'd like to enter.
""")

# Prompt user for number of 1 mile race times they want to enter
num_of_races = int(input("How many 1 mile race times would you like to enter today?: "))

# Set time_sum variable to 0 and set num_of_races_count to num_of_races
time_sum = 0
num_of_races_count = num_of_races

# Prompt user for 1 mile race times in minutes
while num_of_races_count > 0:
    time_sum_input = int(input("Please enter your race time in minutes: "))
    num_of_races_count = num_of_races_count - 1
    time_sum = time_sum + time_sum_input
    print(f"Your total race time so far is {time_sum} minutes.")

# Calculate average 1 mile race time
run_time_avg = time_sum / num_of_races

# Print average 1 mile race time
print(f"Your average run time over {num_of_races} races is {run_time_avg} minutes.")





