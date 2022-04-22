from random import randint

def show_instructions():
    """Shows the game instructions to the player."""

    print("Welcome to the number guessing game!\n")
    print("Instructions:")
    print("- Select a lower and upper bound for a number.")
    print("- Select how many guesses you would like to have. You cannot have more guesses than possible numbers.\n")
    print("The computer will select a random number between the upper and lower bounds (inclusive).")
    print("Can you guess the number before you run out of guesses? :)\n")

def validate_input():
    """Validates the player's input to make sure that an integer value is given."""

    try:
        # Modify to allow decimals that are whole numbers, e.g. 10.0:
        return int(input()) 
    except ValueError: 
        print("Invalid input. Please enter a whole number.")
        return validate_input() # Function is called as many times as is necessary to obtain valid input.

def select_bounds():
    """Enables a player to select lower and upper bounds to guess between."""

    print("Select a lower bound:")
    lower = validate_input() 
    print("Select an upper bound:")
    upper = validate_input() 

    while lower >= upper: 
        print("The upper bound must be greater than the lower bound. Please enter different bounds.\n")
        print("Select a lower bound:")
        lower = validate_input()
        print("Select an upper bound:")
        upper = validate_input()
    
    return (lower, upper)

def select_attempt_number(range):
    """Allows the player to select the number of guesses they can have."""

    print("How many guesses would you like to have?")
    attempts = validate_input()

    while attempts < 1 or attempts > range:
        if attempts < 1:
            print("You need to have at least 1 guess.")
        elif attempts > range:
            print("You cannot have more guesses than possible numbers!") 

        print("Please select a different number of guesses.\n")
        attempts = validate_input()
    
    return attempts

def guess_the_number(lower, upper):
    """Allows the player to guess a number in the range until they guess correctly or run out of guesses."""

    range = upper - lower + 1 # Possible numbers that can be guessed.
    attempts = select_attempt_number(range) # Player can guess how many guess attempts they would like
    answer = randint(lower, upper) # Computer chooses random number in the range for the player to guess
    attempt_counter = 0
    while attempt_counter < attempts:
        print("Guess a number:")
        guess = validate_input()

        if guess < lower or guess > upper:
            print(f"Please guess a number between {lower} and {upper}!")
        else:
            attempt_counter += 1
            if guess == answer:
                print("Congratulations! You guessed correctly!\n")
                break
            else:
                direction = "high" if guess > answer else "low"
                print(f"Incorrect: too {direction}!")
                remaining = attempts - attempt_counter 

                if attempts > 1: 
                    plural_att = "es" * (attempt_counter > 1) #Plural "es" suffix if the user has made more than one guess.
                    plural_rem = "es" * (remaining == 0 or remaining > 1) #Plural "es" suffix if the user has more than one guess or no guesses left.
                    print(f"You have used {attempt_counter} guess{plural_att}. You have {remaining} guess{plural_rem} remaining.") #Ensures a grammatically correct message.

    if guess != answer and attempt_counter == attempts:           
        print(f"You have used up all your guesses! The correct answer was {answer}.\n") 

def play_again_or_not():
    """Allows the player to decide whether or not they want to play the game again."""

    print("You have finished playing the guessing game.")
    again = input("Would you like to play again?").lower() #Allows case-insensitivity.

    while again != "yes" and again != "no":
        print("Invalid response. Please answer either 'yes' or 'no'.")
        again = input("Would you like to play again?").lower()
    
    return again

if __name__ == "__main__":
    
    show_instructions()
    while True:
        bounds = select_bounds() # The bounds between which the player is guessing a number.
        lower = bounds[0]
        upper = bounds[1]

        guess_the_number(lower, upper) # Player tries to guess the number chosen by the computer between the bounds.

        again = play_again_or_not()
        if again == "no":
            break