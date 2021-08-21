# This program will compute the price of a theatre ticket

# Set base ticket_price of 9.75, movie_3d_surcharge of 2.50, and Declare as float
ticket_price = float(9.75)
movie_3d_surcharge = float(2.50)

# Set child_discount of .8, senior_discount of .75, and Declare as float
child_discount = float(0.8)
senior_discount = float(0.75)

# Prompt for patron_age and Declare as int
patron_age = int(input('Please enter your age: '))

# Compute ticket_price
# If age is less than or equal to 10 Compute child ticket_price
if patron_age <= 10:
    ticket_price = ticket_price * child_discount
# If age is greater than or equal to 50 Compute senior ticket_price
if patron_age >= 50:
    ticket_price = ticket_price * senior_discount
# If age is >= 11 or <= 49 Set ticket_price unchanged
else:
    ticket_price = ticket_price

# Prompt for type of movie
movie_3d = input('Is this a 3d movie? [y/n] ')

# If movie_3d is true Compute 3d movie surcharge
if movie_3d == "y":
    ticket_price = ticket_price + movie_3d_surcharge
# If movie_3d is false Set ticket_price unchanged
elif movie_3d == "n":
    ticket_price = ticket_price
# Else End Program if invalid values are entered
else:
    print("You entered an invalid response. Please restart the program and use y or n for your response.")
    exit()

# Write final ticket price based on selections
if patron_age <= 10 and movie_3d == "y":
    print("Your price for a children's 3D movie ticket is: $", "{:.2f}".format(ticket_price))
if patron_age <= 10 and movie_3d == "n":
    print("Your price for a children's movie ticket is: $", "{:.2f}".format(ticket_price))
if patron_age >= 50 and movie_3d == "y":
    print("Your price for a senior's 3D movie ticket is: $", "{:.2f}".format(ticket_price))
if patron_age >= 50 and movie_3d == "n":
    print("Your price for a senior's movie ticket is: $", "{:.2f}".format(ticket_price))
if 11 <= patron_age <= 49 and movie_3d == "y":
    print("Your price for a 3D movie ticket is: $", "{:.2f}".format(ticket_price))
if 11 <= patron_age <= 49 and movie_3d == "n":
    print("Your price for a regular movie ticket is: $", "{:.2f}".format(ticket_price))
