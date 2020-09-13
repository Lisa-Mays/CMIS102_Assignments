# This program will calculate the cost to carpet a room
# given the height and width of the room
# and the users choice of 3 carpet grades

# Set price per square foot for 3 grades of carpet.
# Good grade carpet is 1.25
# Better grade carpet is 2.75
# Best grade carpet is 3.95
carpet_good = 1.25
carpet_better = 2.75
carpet_best = 3.95

# Prompt for width and height of the room in feet
height = float(input("How many feet is the room height?: "))
width = float(input("How many feet is the room width?: "))

# Error checking for positive numbers for room height and width
if height <= 0:
    print("Please enter a room height greater than zero!")
    height = float(input("How many feet is the room height?: "))
elif width <= 0:
    print("Please enter a room width greater than zero!")
    width = float(input("How many feet is the room width?: "))

# Prompt for grade of Carpet (3 choices) good, better, best
print(f"""
There are three grades of carpet to choose from.
The Good carpet costs $ {carpet_good} a square foot. It's pretty Good!
The Better carpet costs $ {carpet_better} a square foot. It's Better!
The Best carpet costs $ {carpet_best} a square foot. It's the Best!
""")
carpet_grade_input = input("Please choose a grade of carpet. (good, better or best): ")


# Function calculate_cost that accepts width, height, and grade as input
# Compute the room carpet cost by multiplying height and width by the carpet grade cost
def calculate_cost(carpet_width, carpet_height, carpet_grade_type):
    carpet_grade = 0
    if carpet_grade_type.lower() == 'good':
        carpet_grade = carpet_good
    elif carpet_grade_type.lower() == 'better':
        carpet_grade = carpet_better
    elif carpet_grade_type.lower() == 'best':
        carpet_grade = carpet_best
    else:
        print("Invalid input.  Please restart program.")
        exit()
    room_cost_calc = (carpet_width * carpet_height * carpet_grade)
    return room_cost_calc


# Call calculate_cost function and Write cost to carpet room
room_cost = calculate_cost(width, height, carpet_grade_input)
print("It will cost $ " + ("{:.2f}".format(room_cost)) + " to carpet your room.")






