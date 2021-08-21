# This program will produce a Halloween Mad Libs from users inputted words.

# Set user_word_list array to empty
user_word_list = []

# Set upper_word_list array to empty
upper_word_list = []

# Set prompt_word_list array to
prompt_word_list = [
    'a Noun', 'a Place', 'a Person', 'an Adjective',
    'a Body Part', 'a Verb', 'an Adjective',
    'a Noun', 'a Food', 'a Plural Noun',
    ]

# Prompt the user for each word in the prompt_word_list and add it to the user_word_list
for word in prompt_word_list:
    user_word_list.append(input(f"Please enter {word}: "))

# Loop through array and capitalize each letter in the array
for user_word in user_word_list:
    upper_word_list.append(user_word.upper())

# Print the mad lib with the users words
print(f"""
I can't believe it's already Halloween!  I can't wait to
put on my {upper_word_list[0]} and visit every {upper_word_list[1]} in
my neighborhood.  This year, I am going to dress up as (a) {upper_word_list[2]}
with {upper_word_list[3]} {upper_word_list[4]}.  Before I {upper_word_list[5]},
I make sure to grab my {upper_word_list[6]} {upper_word_list[7]} to hold all
of my {upper_word_list[8]}.  Finally, all of my {upper_word_list[9]} are ready to go!
""")
