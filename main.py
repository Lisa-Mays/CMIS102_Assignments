# This program calculates years until retirement for ages 18 and over

# Display welcome.  Prompt and Set birth year and current year
# Compute and Set users age
# Declare birth_year and current_year as Int
print('Welcome to the retirement calculator.')
birth_year = int(input('Please enter your birth year: '))
current_year = int(input('Please enter the current year: '))
age = current_year - birth_year

# Prompt for expected retirement age Declare retirement age as int
retirement_age = int(input('Please enter the age you would like to retire: '))

# If age is greater than 18 Compute years until retired
# Set years_left
# Display years until retirement
# Else Display message to come back when 18 years old
if age > 18:
    years_left = retirement_age - age
    print('You have', years_left, 'years left until retirement.')
else:
    print("You aren't old enough to work yet! Come back when you're 18!")
