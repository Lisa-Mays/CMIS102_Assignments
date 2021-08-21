# This program will calculate the bmi of six individuals.
import math

# Set list of 6 names in an array Beth Dad Mom Nicole Lou and Brandy
names = ['Beth', 'Dad', 'Mom', 'Nicole', 'Lou', 'Brandy']
# Set bmi array to empty
bmi = []
# Set underweight bmi max to 19
underweightbmi_max = 19
# Set overweight bmi min to 30
overweightbmi_min = 30
# Set underweight count to 0
underweight_count = 0
# Set overweight count to 0
overweight_count = 0
# Set normal weight count to 0
normalweight_count = 0


# Function to accept height and weight and returns bmi weight x 703 / height squared
def calc_bmi (height, weight):
    # Compute bmi using weight x 703 / height squared
    person_bmi = weight * 703 / math.pow(height, 2)
    return person_bmi
# End Function


# Function to accept BMI and return underweight, normal weight, overweight.
def bmi_definition (bmi_value):
    bmi_result = ""
    if bmi_value < underweightbmi_max:
        bmi_result = 'Underweight'
    elif bmi_value > overweightbmi_min:
        bmi_result = 'Overweight'
    else:
        bmi_result = 'Normal Weight'
    return bmi_result
# End Function


# Main Program

# For loop to prompt for height in inches and weight in pounds and include name in prompt
for person in names:
    input_height = input(f'{person}, please enter your height in inches: ')
    input_weight = input(f'{person}, please enter your weight in pounds: ')
    # Call calc_bmi function
    cur_bmi = calc_bmi(float(input_height), float(input_weight))
    # Append results to bmi array
    bmi.append(cur_bmi)
# End For

# For loop to Compute number of individuals in each category
for each_person_bmi in bmi:
    bmi_text = bmi_definition(each_person_bmi)
    if bmi_text == 'Underweight':
        underweight_count = underweight_count + 1
    elif bmi_text == 'Overweight':
        overweight_count = overweight_count + 1
    elif bmi_text == 'Normal Weight':
        normalweight_count = normalweight_count + 1
# End For

# Display the number of individuals in each category
print(f"The number of underweight individuals is: {underweight_count}")
print(f"The number of normal weight individuals is: {normalweight_count}")
print(f"The number of overweight individuals is: {overweight_count}")

# End Program


