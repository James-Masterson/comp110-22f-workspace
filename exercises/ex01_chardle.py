"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730572598"

user_word: str = input("Enter a 5-character word: ")
enter_letter: str = input("Enter a single character: ")

repeat_letter_counter: int = 0

print("Searching for " + str(enter_letter) + " in " + str(user_word))

if(enter_letter == user_word[0]):
    print(enter_letter + " found at index 0")
    repeat_letter_counter = repeat_letter_counter + 1

if(enter_letter == user_word[1]):
    print(enter_letter + " found at index 1")
    repeat_letter_counter = repeat_letter_counter + 1

if(enter_letter == user_word[2]):
    print(enter_letter + " found at index 2")
    repeat_letter_counter = repeat_letter_counter + 1

if(enter_letter == user_word[3]):
    print(enter_letter + " found at index 3")
    repeat_letter_counter = repeat_letter_counter + 1

if(enter_letter == user_word[4]):
    print(enter_letter + " found at index 4")
    repeat_letter_counter = repeat_letter_counter + 1

if(repeat_letter_counter > 0):
    print(str(repeat_letter_counter) + " instances found in " + user_word)
else:
    print("No instances of " + enter_letter + " found in " + user_word)