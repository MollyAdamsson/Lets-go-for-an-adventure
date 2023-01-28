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

def path_choice_2():
    print("\033[35m" + "The air is damp and filled with the scent of old trees" + "\033[0m")
    print("\033[35m" + "The soft rustling of leaves scared you a bit, anything could be hiding in the bushes" + "\033[0m")
    print("\033[35m" + "You get further in to the forest, there are huge tree logs laying everywhere." + "\033[0m")
    print("\033[35m" + "There is one big one in the middle of the road, you have to climb over it to keep going" + "\033[0m")
    print("\033[35m" + "Type '1' for yes to climb the log or type '2' to go another way." + "\033[0m")
    while True:
        choice = input("> ")
        if choice == '1':
            clearConsole()
            path_choice_3()
            break
        elif choice == '2':
            clearConsole()
            path_choice_4()
            break
        else:
            print("\033[31mInvalid choice, please type '1' or '2'\033[0m")
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

def player_encounter_goblin():
    goblin_health = 40
    goblin_attack = 15
    print("\033[31mYou have come across a nasty forest goblin!\033[0m")
    print("\033[31mDo you want to attack or run away?\033[0m")
    print("\033[31mEnter 'a' to attack or 'r' to run away!\033[0m")
    choice = input("\033[31m>\033[0m ")
    while goblin_health > 0:
        if choice == 'a':
            global player_health
            player_attack = random.randint(10, 14)
            goblin_health -= player_attack
            if goblin_health <= 0:
                clearConsole()
                print("\033[32mYou have defeated the goblin! You may continue on your journey.\033[0m")
                print("\033[32mYou have received a 'Badge of Honor', only brave ones get this.\033[0m")
                print("\033[32mDo you want to continue your journey? Enter '1' for yes and '2' for no and end game.\033[0m")
                while True:
                    choice = input("\033[32m>\033[0m ")
                    if choice == '1':
                        meet_wizard()
                        break
                    elif choice == '2':
                        game_over()
                        break
                    else:
                        print("\033[31mInvalid choice, please enter '1' or '2'\033[0m")
                        continue
            else:
                print("\033[31mThe goblin now has " + str(goblin_health) + " health.\033[0m")
                player_health -= goblin_attack
            if player_health <= 0:
                    clearConsole()
                    player_death()
            else:
                print("\033[31mYou now have " + str(player_health) + " health.\033[0m")
                print("\033[31mDo you want to attack or run? Enter 'a' to attack and 'r' to run.\033[0m")
                choice = input("\033[31m>\033[0m ")
        elif choice == 'r':
            run_away_chance = random.randint(10,14)
            if run_away_chance <= 30:
                clearConsole()
                print("\033[32mYou managed to run away safely from the goblin.\033[0m")
                print("\033[32mDo you want to continue your journey? Enter '1' for yes and '2' for no and end game.\033[0m")
                choice = input("\033[32m>\033[0m ")
                if choice == '1':
                    meet_wizard()
                elif choice == '2':
                    game_over()
                else:
                    print("\033[31mInvalid choice, please enter '1' or '2'\033[0m")
                    choice = input("\033[31m>\033[0m ")
            else:
                clearConsole()
                print("\033[31mYou failed to run away and the goblin hit you.\033[0m")
                player_health -= goblin_attack
                if player_health <= 0:
                    player_death()
                else:
                    print("\033[31mYou now have {player_health} health.\033[0m")
                    print("\033[31mDo you want to attack or run? Enter 'a' to attack and 'r' to run.\033[0m")
                    choice = input("\033[31m>\033[0m ")
        else:
            print("\033[31mInvalid choice, please type 'a' or 'r'\033[0m")
            choice = input("\033[31m>\033[0m ")


        
start_game()