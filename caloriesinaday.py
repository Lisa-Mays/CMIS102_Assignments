# Write Welcome to the Calorie Counter, a program to calculate calories consumed in one day
print ('Welcome to the Calorie Counter!')

# Prompt the user for total breakfast calories
breakfast_calories = eval(input('Please enter the total calories for breakfast: '))

# Prompt the user for total lunch calories
lunch_calories = eval(input('Please enter the total calories for lunch: '))

# Prompt the user for total dinner calories
dinner_calories = eval(input('Please enter the total calories for dinner: '))

# Prompt the user for total snack calories
snack_calories = eval(input('Please enter the total calories for snacks: '))

# Compute the breakfast, lunch, dinner, and snack values and Set total calories
total_calories = breakfast_calories + lunch_calories + dinner_calories + snack_calories

# Write the total calorie results
print ('Your total calories for the day: ', total_calories)