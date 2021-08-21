# This Program will count how many vowels are in a given word
# Welcome
print("Welcome to the word vowel counter!")

# Prompt the user for a word
user_word = input("Please enter a word: ")

# Count Number of letters in the word
word_length = len(user_word)

# Define what vowels are
vowels = "aeiou"
sometimes_y = "y"

# Set vowel_count to 0 Set char_index to 0 Set sometimes_vowel to 0
vowel_count = 0
char_index = 0
sometimes_vowel = 0

# Check each letter for vowels and Display found vowels
for char_index in range(word_length):
    cur_char = user_word[char_index]
    if cur_char in vowels:
        vowel_count = vowel_count + 1
        print(f"{cur_char} is a vowel")

if vowel_count == 0:
    for char_index in range(word_length):
        cur_char = user_word[char_index]
        if cur_char in sometimes_y:
            sometimes_vowel = sometimes_vowel + 1
            print(f"{cur_char} is a vowel")

# Compute number of vowels then Display number of vowels
if vowel_count > 0:
    print(f"There are {vowel_count} vowels in your word!")
else:
    print(f"There are {sometimes_vowel} vowels in your word!")


