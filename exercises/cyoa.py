"""My CYOA for exercise 6 is a random number guessing game."""

__author__ = "730572598"

from random import randint

player: str = ""
points: int = 0
path: int = 0
STAR_CODE: str = ""
is_running: bool = True
runs: int = 0
average_points: int = 0


def main() -> None:
    """This is the main function that drives the whole program."""    
    global path

    greet()
    
    while (is_running is True):
        print("If you would like to try and guess a high number (1-100), then type '0'.")
        print("If you would like to try and guess a lower number (1-10), then type '1'.")
        print("If you would like to exit this game, then type '2'.")
        path = int(input("What option would you like to choose?: "))
        
        game_mechanics(path)

    while (path < 0 or path > 2):
        path = int(input("That was not an available option. Type either '0', '1', or '2': "))
        

def game_mechanics(path: int) -> int:
    """This is where the main guessing game mechanics are written/take place."""
    global is_running
    global points
    global STAR_CODE
    global runs
    global average_points
    secret_number: int = 0
    stars: str = ""
    STAR_CODE = "\U00002B50"
    guesses: int = 0

    if (path == 0):
        guesses = 0
        secret_number = randint(1, 100)
        print("You've chosen to guess a number between 1-100")
        guess: int = int(input("What is your guess?: "))

        while (guess != secret_number):
            if (guess == -1):
                print("You have exited out of the program. If you would like to play again, please re-run.")
                is_running = False
            else:
                if (guess < secret_number):
                    guesses += 1
                    guess = int(input(f"Your guess, {guess}, was too low! Guess higher!: "))
                else:
                    guesses += 1
                    guess = int(input(f"That guess, {guess}, was too high! Guess lower!: "))
        else: 
            guesses += 1
            if (guesses <= 5):
                points += 100
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 7):
                points += 85
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 9):
                points += 70
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 11):
                points += 55
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 13):
                points += 40
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 15):
                points += 25
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points

    if (path == 1):
        guesses = 0
        secret_number = randint(1, 10)
        print("You've chosen to guess a number between 1-10.")
        guess: int = int(input("What is your guess?: "))
        
        while (guess != secret_number):
            if (guess == -1):
                print("You have exited out of the program. If you would like to play again, please re-run.")
                is_running = False
            else:
                if (guess < secret_number):
                    guesses += 1
                    guess = int(input(f"Your guess, {guess}, was too low! Guess higher!: "))
                else:
                    guesses += 1
                    guess = int(input(f"That guess, {guess}, was too high! Guess lower!: "))
        else: 
            guesses += 1
            if (guesses <= 3):
                points += 100
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 4):
                points += 85
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 5):
                points += 70
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 6):
                points += 55
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 7):
                points += 40
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points
            elif (guesses >= 8):
                points += 25
                print(f"You have been awarded {points} points for your performance, {player}!")
                runs += 1
                return points

    if (path == 2):
        if (points // runs > 85):
            stars += STAR_CODE
        if (points // runs > 70):
            stars += STAR_CODE
        if (points // runs > 55):
            stars += STAR_CODE
        if (points // runs > 40):
            stars += STAR_CODE
        if (points // runs > 25):
            stars += STAR_CODE
        if (points // runs <= 25):
            stars += "NO"
        average_points = points // runs

        print(f"You finished with {points} points and you averaged {average_points} points on average. You have been awarded {stars} stars for your performance, {player}!")
        print("System Exit: Play again soon!")
        stars = ""
        runs = 0
        guesses = 0
        is_running = False


def greet() -> None:
    """This function prints a greet message on the screen and then asks the user what path they would like to choose."""
    global player 
    player = input("What is your name?: ")

    print(f"Hello {player}! This is a number guessing game where you will try to find the secret number! Here are some of the basic rules: ")
    print("You will start with 100 adventure points at the beginning of the game. For each incorrect guess you make, you will lose a certain amount of adventure points.")
    print("(This depends on which number range you pick. If you decide to try and guess a number within 1-100, you will lose 3 adventure points per guess.")
    print("If you decide to guess a number within the 1-10 range, you will lose 10 points per incorrect answer.)")
    print("If you want to exit the game early, type in '-1' to end the program.")
    print("Depending on how many adventure points you have when you guess the correct answer, you will earn 0-5 stars for your performance.")
    print("This is also dependent on the number-range you choose.")


if __name__ == "__main__":
    main()