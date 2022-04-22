from random import randint

def validate_input():
    """
    Validates the user input to make sure that an integer value is given.
    """
    try:
        return int(input()) 
    except ValueError: 
        print("Invalid input. Please enter a whole number.")
        return validate_input() #Function is called as many times as is necessary to obtain valid input.

print("Welcome to the number guessing game!\n")
print("Instructions:")
print("- Select a lower and upper bound for a number.")
print("- Select how many guesses you would like to have. You cannot have more guesses than possible numbers.\n")
print("The computer will select a random number between the upper and lower bounds (inclusive).")
print("Can you guess the number before you run out of guesses?\n")

while True:
    print("Select a lower bound:")
    lower = validate_input() 
    print("Select an upper bound:")
    upper = validate_input() 

    while lower > upper: 
        print("The upper bound must be greater than the lower bound. Please enter different bounds.\n")
        print("Select a lower bound:")
        lower = validate_input()
        print("Select an upper bound:")
        upper = validate_input()

    answer = randint(lower, upper) 

    print("How many guesses would you like to have?")
    attempts = validate_input() 
    range = upper - lower + 1 #Possible numbers that can be guessed.

    while attempts < 1 or attempts > range:
        if attempts < 1:
            print("You need to have at least 1 guess.")
        elif attempts > range:
            print("You cannot have more guesses than possible numbers!") 

        print("Please select a different number of guesses.\n")
        attempts = validate_input()

    attempt_counter = 0 #Tracks how many guesses the user has made.

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

    print("You have finished playing the guessing game.")
    again = input("Would you like to play again?").lower() #Allows case-insensitivity.

    while again != "yes" and again != "no":
        print("Invalid response. Please answer either 'yes' or 'no'.")
        again = input("Would you like to play again?").lower()
    
    if again == "no":
        break