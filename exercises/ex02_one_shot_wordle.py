"""EX02 - One Shot Wordle - A cute step toward Wordle."""

__author__ = "730572598"

secret_word: str = "python"

user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

i: int = 0


word_boxes: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while (len(user_guess) != len(secret_word)): 
    user_guess = input(f"The was not {len(secret_word)}-letters! Try again: ")

while (i < len(secret_word)):
    if (user_guess[i] == secret_word[i]):
        word_boxes += GREEN_BOX
    else:
        added_boxes: bool = False
        n: int = 0 
        while n < len(secret_word):
            if (user_guess[i] == secret_word[n]):
                added_boxes = True
            n += 1
        if (added_boxes is True):
            word_boxes += YELLOW_BOX
        else:
            word_boxes += WHITE_BOX

    i += 1
print(word_boxes)
    

if (user_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")