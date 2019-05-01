import os
import constants
constants.print_team()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def team_builder():

    Panthers = []
    Bandits = []
    Warriors = []
    
    with open("constants.py") as file:
        for index in file:
            print(index)

def teams_options():
    while True:
        try:
            print("1) Panthers")
            print("2) Bandits")
            print("3) Warriors\n")
            team_choice = int(input("Enter an option > "))
            if team_choice == 1:
                panthers_stat()  # A Function here
            elif team_choice == 2:
                bandit_stat()  # A Function here
            elif team_choice == 3:
                warrior_stat()  # A Function here
            else:
                print("That's not a valid option. Please enter a number either 1 to 3.")
        except ValueError:
            print("That's not a number... Please enter a number either 1 or 2.")


def start():
        print(" BASKETBALL TEAM STATS TOOL\n")
        print("-"*28)
        print("         - MENU -")
        print("-"*28)
        print("")
        while True:
            try:
                print("Here are your choices:")
                print(" 1) Display Team Stats\n 2) Quit\n\n")

                menu_choice = int(input("Enter an option > "))
                if menu_choice <= 0 or menu_choice > 2:
                    print("That's not a valid option. Please enter a number either 1 or 2.")
                    continue
                elif menu_choice == 1:
                    teams_options()
                else:
                    break
            except ValueError:
                print("That's not a number... Please enter a number either 1 or 2.")
            else:
                break


if __name__ == "__main__":
    start()
