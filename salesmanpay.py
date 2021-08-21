# This program calculates a salesman's weekly pay with a fixed hourly
# rate and a fixed commission percentage

# Set hourly rate to 27 dollars per hour Declare hourly_rate as float
hourly_rate = float(27.00)

# Set commission percentage to 25 percent
commission_percentage = 0.25

# Prompt for hours worked Declare hours_worked as int
hours_worked = int(input('Please enter your number of hours worked for this week: '))

# Prompt for total weekly sales Declare weekly_sales as float
weekly_sales = float(input('Please enter your total sales for this week: $'))

# Compute hourly rate and weekly commission and Set hourly pay, commission pay, and weekly pay
hourly_pay = hours_worked * hourly_rate
commission_pay = weekly_sales * commission_percentage
weekly_total_pay = hourly_pay + commission_pay

# Write hours worked, commission, and total pay for the week
print('Your total hours worked are: ', hours_worked)
print('Your hourly rate is : $', "{:.2f}".format(hourly_rate), "an hour")
print('Your base pay based on hours worked this week is: $', ("{:.2f}".format(hourly_pay)))
print('Your commission percentage of weekly sales is: ', commission_percentage, '%')
print('Your total commission for the week is: $', "{:.2f}".format(commission_pay))
print('Your total pay for the week is: $', "{:.2f}".format(weekly_total_pay))