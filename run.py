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

    '''First path that leads the player to the next path'''

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

    '''Path choice 2, here the player has to make 
    a choice if the want to go to path 3 or 4'''

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

def path_choice_3():

    '''New path that lead the player to the enemy/goblin encounter'''

    print("\033[35mYou can barely see anything now, the light that once shined through the tree tops is now a distant memory")
    print("This is the last time I leave my house, you mutter. It's just not worth it")
    print("You keep on walking, jumping over the big branches streching over the pathway")
    print("You sense that you are not alone, someone is watching you. But where?")
    print("You stop in your tracks, the smell of something rotten hits you!")
    print("Do you want to keep going? Type 'y' for yes or 'n' for no and run away.\033[0m")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            player_encounter_goblin()
            break
        elif choice == 'n':
            clearConsole()
            print("You have no choice")
            player_encounter_goblin()
            break
        else:
            print("\033[31mInvalid choice, please type 'y' or 'r'\033[0m")
            continue

def path_choice_4():

    '''New path that introduces the player to an owl that will give them som
    inspiring words to keep on going + leads to meet the Witch'''

    print("\033[35mYou keep walking on what you think is the path, you are not sure.")
    print("It doesn't seem like anyone has been here for years")
    print("the roots of the trees are everywhere.")
    print("All of a sudden you see an old owl sitting on a branch.")
    print("It clears its throat and says:") 
    print("\033[36m\"Hello there brave one, I've been waiting for you!\"\033[0m")
    print("\033[36m\"To get to the end you must be even braver, hold on!\"\033[0m")
    print("\033[35mType 'l' to go left or 'f' to go forward")
    while True:
        choice = input("> \033[0m")
        if choice == 'l':
            clearConsole()
            meet_witch()
            break
        elif choice == 'f':
            print("\033[31mThe trees grow too dense here, you can't get through\033[0m")
            print("\033[31mYou have to take another path\033[0m")
            print("\033[31mChoose 'l' to go left\033[0m")
            while True:
                choice = input ("> ")
                if choice == 'l':
                    clearConsole()
                    meet_witch()
                    break
                else:
                    print("\033[1;31;40mInvalid choice, please type 'l' to keep going\033[0;37;40m")
                    continue
        else:
            print("\033[91mInvalid choice, please type 'l' or 'f'\033[0m")
            continue

def path_choice_5():
    print("You move along, wondering what the beautiful Witch meant")
    print("How many times will you rise and fall?")
    print("You study the the binders of the book when all of a sudden")
    print("three small forest gnomes appear, right in fron of you")
    print("You: \"Hello, can I help you\" ")
    print("The gnomes look at each other, and then back at you")
    print("Then all of them open their mouths an at the same time they say: ")
    print(" \"You have to hurry, he is waiting for you\"")
    print("You:\"Huh, who is?\" ")
    print("\"You will find out soon, just hurry!\" They say.")
    print("They then grab each others hands and scurries off")
    print("You stand still for quick moment, wondering what just happend")
    print("You then say to yourself: ")
    print("\"Well I cant stay here, can I? I have to keep going\"")
    print("Do you want to continue? typ 'y' for yes and 'n' for no and end game")
    while True:
        choice = input("> ")
        if choice == 'y':
            meet_wizard()
            break
        elif choice == 'n':
            game_over()
            break
        else:
            print("invalid choice, please type 'y' or 'n'")
            continue

def riddle_encounter():

    '''Solve the riddle, gives different options + a valuable treasure'''

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
            print("\033[32mYou put it in your backpack and start walking again.\033[0m")
            path_choice_2()
            break
        else:
            print("\033[32mIncorrect. You have failed the task.\033[0m")
            game_over()


def player_encounter_goblin():

    '''Player meets the goblin/enemy'''

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

def meet_witch():
    '''
    Function that introduce the witch, 
    here the player is given a book and an option to proceed to the Wizard
    '''
    print("\033[35mA beautiful woman appears\033[0m")
    print("\033[35mWith a soft smile she says:")
    print("\033[36m\"Ah the wispers were right\" ")
    print("\033[36m\"There is a human here, I've been looking all over for you\" ")
    print("\033[36m\"I need to tell you something, a few words of wisdom to keep in mind\"")
    print("\"You ready? Okay, listen closely\"")
    print("\"The greatest glory in living lies not in never falling, but in rising every time we fall\"")
    print("\"You need to remember this for the rest of your journey, okay\"?")
    print("\"Matter of fact, take this book, it is filled with knowledge\"\033[0m")
    print("\033[35mYou have collected the book of wisdom. It has been added to your inventory")
    print("\033[35mSuddenly the beautiful witch disapears and you're all alone")
    print("\033[35mDo you want to continue your journey? Enter 'y' for yes or 'n' for no.")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            path_choice_5()
            break
        elif choice == 'n':
            clearConsole()
            game_over()
            break
        else:
            print("\033[31mInvalid choice, please type 'y' or 'n'")
            continue
               
start_game()