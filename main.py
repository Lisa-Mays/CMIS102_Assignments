# This program will test a given password to be sure it meets minimum requirements

# Write welcome message
print("Welcome to the password tester!")

# Set min_pass_length to 8
min_pass_length = 8

# Set max_pass_length to 15
max_pass_length = 15

# Set forbidden_phrase to umgc
forbidden_phrase = 'umgc'

# Set must_contain_pound to #
must_contain_pound = '#'

# Set input_password_length to 0
input_pass_length = 0


# Function to Write the password requirements
def pass_requirements():
    print("""
Your password needs to be between 8 and 15 characters long. 
It must have a '#' symbol but it cannot be in the first or last position.
Your password cannot contain the phrase 'UMGC' or 'umgc'.
    """)
# End Function


# Function to Prompt the user for a password
def ask_for_password():
    input_password = input("Please enter a password: ")
    return input_password
# End Function


# Function to validate password
def validate_password(check_password):
    password_is_valid = True
    # Check If password is at least min length
    if len(check_password) < min_pass_length:
        # Write failed validation message
        print(f"Your password must be greater than {min_pass_length} characters.")
        # Set password_is_valid to false
        password_is_valid = False

    # Check If password isn't longer than max length
    if len(check_password) > max_pass_length:
        # Write failed validation message
        print(f"Your password must be less than {max_pass_length} characters.")
        # Set password_is_valid to false
        password_is_valid = False

    # Check If UMGC or umgc is in the password
    if forbidden_phrase.lower() in check_password.lower():
        # Write failed validation message
        print(f"Your password cannot contain the phrase 'UMGC' or 'umgc'.")
        # Set password_is_valid to false
        password_is_valid = False

    # Check If '#' is in the password
    if must_contain_pound not in check_password:
        # Write failed validation message
        print(f"Your password must contain the symbol {must_contain_pound}.")
        # Set password_is_valid to false
        password_is_valid = False

    # Check If '#' is in the first position or last position
    if must_contain_pound == check_password[0] or check_password.endswith(must_contain_pound):
        # Write failed validation message
        print(f"Your password cannot start with or end with {must_contain_pound}.")
        # Set password_is_valid to false
        password_is_valid = False

    return password_is_valid
# End Function


# Main

# Call pass_requirements
pass_requirements()


# Call ask_for_password
user_password = ask_for_password()

# Call validate_password
if validate_password(user_password):
    # Write pass message
    print("Congrats! Your password meets all of the requirements and is valid.")
else:
    # Write fail message
    print("Bad password!  This password is not valid.")

# End Program



