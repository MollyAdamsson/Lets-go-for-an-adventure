import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command ='cls'
    os.system(command)

player_health = 70
player_attack = 10
player_defense = 5
player_inventory = ["A healing potion"]

def start_game():
    '''Introduction and initial setup to game, introuces the rules and mission'''
    print("\033[32m<b>Welcome to the adventure game!<b>033[0m")
    print("\033[32mYou are now about to embark on an epic journey filled with challanges and obstacles.033[0m")
    print("\033[32mThe goal is to complete each task and get to the other side \nof the woods so you can get home.033[0m")
    print("\033[32mThis is the adventure of a life time!033[0m")
    player_name = input("\033[32mWhat is your name?\033[0m ")
    clearConsole()
    print("\033[32m" + f"Welcome " + str(player_name) + " to the Damned Willow Forest!" + "\033[0m")
    print("\033[32m" + "You are staring at the dense growing trees, wondering how you will get by." + "\033[0m")
    print("\033[32m" + "The first thing you see is a signpost that warns you about the many obstacles" + "\033[0m")
    print("\033[32m" + "you may meet inside and that you have to overcome them to continue on your journey." + "\033[0m")
    print("\033[32m" + "They will test your skills and determination so you can get home." + "\033[0m")
    print("\033[32m" + "Take a deep breath, and let the adventure begin!" + "\033[0m")
    choice = input("\033[32m" + "Are you ready? Type 'y' for yes or 'n' for no > " + "\033[0m")
    if choice == 'y':
        clearConsole()
        print("\033[32m" + "Here is some valid information about your character: \n Health: " + str(player_health) + "\n Attack: " + str(player_attack) + "\n Defense: " + str(player_defense) + "\n Inventory: " + str(player_inventory) + "\033[0m")
        input("\033[32m" + "Press any key to enter the woods: " + "\033[0m")
        clearConsole()
        path_choice()
    elif choice == 'n':
        print("\033[32m" + "Thanks for playing! Have a good day!" + "\033[0m")
        game_over()
    else:
        print("\033[31m" + "Invalid choice, please type 'y' for yes or 'n' for no" + "\033[0m")
    return
