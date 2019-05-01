import os
from constants import TEAMS, PLAYERS

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def panthers_stats():
    panthers_team = PLAYERS[:6]
    print("Team: {} Stats".format(TEAMS[0]))
    print("-"*24)
    print("Total players {}\n".format(len(panthers_team)))
    print("Players on Team:")
    print("")
    enterToContinue()


def bandits_stats():
    bandits_team = PLAYERS[6:12:]
    print("Team: {} Stats".format(TEAMS[1]))
    print("-"*24)
    print("Total players {}\n".format(len(bandits_team)))
    print("Players on Team:")
    print("")
    enterToContinue()


def warriors_stats():
    warriors_team = PLAYERS[-6:]
    print("Team: {} Stats".format(TEAMS[2]))
    print("-"*24)
    print("Total players {}\n".format(len(warriors_team)))
    print("Players on Team:")
    print("")
    enterToContinue()


def enterToContinue():
    while True:
        moveOn = input("Press ENTER to continue...")
        if moveOn == "":
            clear_screen()
            teams_options()
        elif moveOn == str or int:
            print("You didn't press ENTER. Please press ENTER to continue")
    

def teams_options():
    while True:
        try:
            print("1) Panthers")
            print("2) Bandits")
            print("3) Warriors\n")
            team_choice = int(input("Enter an option > "))
            if team_choice == 1:
                panthers_stats()  # A Function here
            elif team_choice == 2:
                bandits_stats()  # A Function here
            elif team_choice == 3:
                warriors_stats()  # A Function here
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
