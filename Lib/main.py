# This program will calculate the cost to carpet a room
# given the height and width of the room
# and the choice of carpet grades

# Set price per square foot for 3 grades of carpet
carpet_good = 1.25
carpet_better = 2.75
carpet_best = 3.95

# Prompt for width and height of the room in feet
height = int(input("How many feet is the room height?: "))
width = int(input("How many feet is the room width?: "))

# Pick Grade of Carpet (3 choices) good, better, best
print(f"""
There are three grades of carpet to choose from.
The Good carpet costs $ {carpet_good} a square foot. It's pretty Good!
The Better carpet costs $ {carpet_better} a square foot. It's Better!
The Best carpet costs $ {carpet_best} a square foot. It's the Best!
""")
carpet_grade = input("Please choose a grade of carpet. (good, better or best): ")
if carpet_grade.lower() == 'good':
    carpet_grade = carpet_good
elif carpet_grade.lower() == 'better':
    carpet_grade = carpet_better
elif carpet_grade.lower() == 'best':
    carpet_grade = carpet_best
else:
    print("Invalid input.  Please restart program.")
    exit()

# Compute cost Function that multiplies height and width by the carpet cost

def calculate_cost():
    room_cost = width * height * carpet_grade
    return room_cost


# Write cost to carpet room
room_cost = calculate_cost()
print(f"It will cost $ {room_cost} to carpet your room.")






