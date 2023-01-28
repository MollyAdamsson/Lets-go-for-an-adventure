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
    print("\033[32mWelcome to the adventure game!")
    print("\033[32mYou are now about to embark on an epic journey.")
    print("\033[32mfilled with challanges and obstacles.")
    print("\033[32mThe goal is to complete each task and get to the other side \nof the woods so you can get home.")
    print("\033[32mThis is the adventure of a life time!")
    player_name = input("\033[32mWhat is your name?\"")
    clearConsole()
    print("\033[32m" + f"Welcome " + str(player_name) + " \nto the Damned Willow Forest!" + "\033[0m")
    print("\033[32m" + "You are staring at the dense growing trees," + "\033[0m")
    print("\033[32m" + "wondering how you will get by." + "\033[0m")
    print("\033[32m" + "The first thing you see is a signpost that warns \nyou about the many obstacles" + "\033[0m")
    print("\033[32m" + "you may meet inside and that you have to overcome \nthem to continue on your journey." + "\033[0m")
    print("\033[32m" + "They will test your skills and determination so you can get home." + "\033[0m")
    print("\033[32m" + "Take a deep breath, and let the adventure begin!" + "\033[0m")
    
    while True: 
        choice = input("\033[32m" + "Are you ready? Type 'y' for yes or 'n' for no > " + "\033[0m")
        if choice == 'y':
            clearConsole()
            print("\033[32m" + "Here is some valid information about your character: \n Health: " + str(player_health) + "\n Attack: " + str(player_attack) + "\n Defense: " + str(player_defense) + "\n Inventory: " + str(player_inventory) + "\033[0m")
            input("\033[32m" + "Press any key to enter the woods: " + "\033[0m")
            clearConsole()
            path_choice()
            break
        elif choice == 'n':
            print("\033[32m" + "Thanks for playing! Have a good day!" + "\033[0m")
            game_over()
            break
        else:
            print("\033[31m" + "Invalid choice, please type 'y' for yes or 'n' for no" + "\033[0m")
            clearConsole()
            continue

def path_choice():
    print("\033[32mLets get started. Do you want to move forward? Type 'y' for yes and 'n' for no and quit game\033[0m")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            riddle_encounter()
            break
        elif choice == 'n':
            game_over()
            break
        else:
            print("\033[31mInvalid choice, please type 'y' or 'n'\033[0m")
            continue

def riddle_encounter():
    riddles = ["What starts with an E, ends with an E, but only contains one letter?"]
    riddle = random.choice(riddles)
    print("\033[32mYou come across a treasure chest and a sign with a riddle written on it, to open the chest you must answer correctly!\033[0m")
    print("\033[32m" + riddle + "\033[0m")
    print("\033[32m1. Elephant\033[0m")
    print("\033[32m2. Envelope\033[0m")
    print("\033[32m3. Eagle\033[0m")
    print("\033[32m4. Edge\033[0m")
    while True:
        answer = input("\033[32mWhat is your answer?\033[0m ")
        if answer.lower() == "2":
            clearConsole()
            print("\033[32mCorrect! The chest is open! You collect the treasure inside!\033[0m")
            print("\033[32mThe treasure is shiny and heavy. It must be worth alot.\033[0m")
            print("\033[32mYou put in your backpack and start walking again.\033[0m")
            path_choice_2()
            break
        else:
            print("\033[32mIncorrect. You have failed the task.\033[0m")
            game_over()
            continue
        


        
start_game()