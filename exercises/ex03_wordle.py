"""EX03 - Structured Wordle - The final step into creating Wordle."""

__author__ = "730572598"


def contains_char(user_word: str, find_match: str) -> bool:
    """This function establishes the variables that will be used within the Wordle program."""
    assert len(find_match) == 1
    i: int = 0
    same_letter_found: bool = False
    while (i < len(user_word)):
        if (find_match == user_word[i]):
            same_letter_found = True
        i += 1
    if (same_letter_found is True):
        return True
    else:
        return False


def emojified(user_guess: str, actual_word: str) -> str:
    """Responsible for creating the colored boxes according to the user's guesses."""
    assert len(user_guess) == len(actual_word)
    
    x: int = 0
    word_boxes: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while (x < len(actual_word)):
        if (user_guess[x] == actual_word[x]):
            word_boxes += GREEN_BOX
        else:
            add_box: bool = contains_char(actual_word, user_guess[x])
            
            if (add_box is True):
                word_boxes += YELLOW_BOX
            else:
                word_boxes += WHITE_BOX
        x += 1
    
    return word_boxes


def input_guess(expected_length: int) -> str:
    """Makes sure that guesses are only of the same length as the same word."""
    word: str = input(f"Enter a {expected_length} character word: ")

    while (len(word) != expected_length):
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    else:
        return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    user_win: bool = False
    

    while (turns < 7):
        if (user_win is not True):
            print(f"=== Turn {turns}/6 ===")
            final_guesses: str = input_guess(len(secret_word))
            emojified(final_guesses, secret_word)
            if (final_guesses == secret_word):
                print(f"You won in {turns}/6 turns!")
                user_win = True
        turns += 1
    
    if (user_win is not True):
        print("X/6 - Sorry try again tomorrow!")

if __name__ == "__main__":
    main()