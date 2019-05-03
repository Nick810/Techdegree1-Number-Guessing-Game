# Techdegree Project 1

import random


highscores = []

def start_game():

    guess_count = []
    new_highscores = len(guess_count)

    from random import randint
    CORRECT_NUMBER = randint(1,10)

    if highscores:
        print("Your HIGHSCORE is", (min(highscores)))

    print("-"*35)
    print("Welcome to the Number Guessing Game")
    print("-"*35)
    print("")

    while True:
        guessed_number = number_guess()
        guess_count.append(guessed_number)
        if guessed_number < CORRECT_NUMBER:
            print("It's higher!")
        elif guessed_number > CORRECT_NUMBER:
            print("It's lower!")
        else:
            print("You've got it! It took you {} tries".format(len(guess_count)))
            new_highscores = len(guess_count)
            highscores.append(new_highscores)
            prompt = str(input("Would you like to play more? [y]es/[n]o "))
            if prompt.lower() == 'yes' or prompt.lower() == 'y':
                print("\n\n")
                start_game()
            else:
                print("Hope that was fun! :P, Bye Now!")
            break

            
def number_guess():
    while True:
        try:
            guessed_number = int(input("Pick a number between 1 and 10: "))
            if guessed_number <= 0 or guessed_number > 10:
                print("That's out of range! Please enter a number between 1 and 10.")
                continue
            break
        except ValueError:
            print("That's a not number... Please enter a number between 1 and 10!")

    return guessed_number


if __name__ == '__main__':
    start_game()
