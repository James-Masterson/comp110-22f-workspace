"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730572598"

user_word: str = input("Enter a 5-character word: ")
repeat_letter_counter: int = 0

if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
else:
    enter_letter: str = input("Enter a single character: ")
    if (len(enter_letter) == 1):
        print("Searching for " + enter_letter + " in " + user_word)
        if (enter_letter == user_word[0]):
            print(enter_letter + " found at index 0")
            repeat_letter_counter = repeat_letter_counter + 1
        if (enter_letter == user_word[1]):
            print(enter_letter + " found at index 1")
            repeat_letter_counter = repeat_letter_counter + 1
        if (enter_letter == user_word[2]):
            print(enter_letter + " found at index 2")
            repeat_letter_counter = repeat_letter_counter + 1
        if (enter_letter == user_word[3]):
            print(enter_letter + " found at index 3")
            repeat_letter_counter = repeat_letter_counter + 1
        if (enter_letter == user_word[4]):
            print(enter_letter + " found at index 4")
            repeat_letter_counter = repeat_letter_counter + 1
        if (repeat_letter_counter == 1):
            print(str(repeat_letter_counter) + " instance of " + enter_letter + " found in " + user_word)
        if (repeat_letter_counter == 0):
            print("No instances of " + enter_letter + " found in " + user_word)
        if (repeat_letter_counter > 1):
            print(str(repeat_letter_counter) + " instances of " + enter_letter + " found in " + user_word)
    else:
        print("Error: Character must be a single character.")
        exit()