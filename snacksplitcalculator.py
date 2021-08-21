# This program calculates how many snacks are leftover at snack time

# Input snack 1 name
snack1 = input("Please enter the name of the first snack: ")
# Input snack 1 amount
snack1_amt = int(input("Please enter the amount of " + snack1 + ": "))
# Input snack 2 name
snack2 = input("Please enter the name of the second snack: ")
# Input snack 2 amount
snack2_amt = int(input("Please enter the amount of " + snack2 + ": "))
# Input snack 3 name
snack3 = input("Please enter the name of the third snack: ")
# Input snack 3 amount
snack3_amt = int(input("Please enter the amount of " + snack3 + ": "))

# Input the number of kids to divide the snacks between
kids = int(input("Please enter the number of children: "))

# Call math function and Compute greatest common denominator Declare bestgcd as str
import math
total_snacks = snack1_amt + snack2_amt + snack3_amt
divided_snacks = total_snacks // kids
leftover_snacks = math.remainder(total_snacks, kids)
divided_snacks = str(divided_snacks)


# Write largest number of snacks that can be put on each plate
print("You can put " + divided_snacks + " snacks on each plate.")
# If there are leftover snacks for the teacher Write the amount
if leftover_snacks > 0:
    print("The teacher can have " + str(leftover_snacks) + " leftover snacks!")
# Else if there aren't any leftover snacks Write a sorry message
elif leftover_snacks == 0:
     print("Oh no! There are " + str(leftover_snacks) + " snacks for the teacher today!")

