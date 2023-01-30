import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


player_health = 70
player_attack = 10
player_defense = 5


def start_game():

    '''Introduction and initial setup to game, rules and mission'''

    print("\033[32mWelcome to the adventure game!")
    print("\033[32mYou are now about to embark on an epic journey.")
    print("\033[32mfilled with challanges and obstacles.")
    print("\033[32mThe goal is to complete each task and get to the other side \nof the woods so you can get home.")
    print("\033[32mThis is the adventure of a life time!")
    player_name = input("\033[32mWhat is your name?\"")
    clearConsole()
    print("\033[32m" + f"Welcome " + str(player_name) + " ""\033[0m")
    print("\033[32m" + f"to the Damned Willow Forest!" + "\033[0m")
    print("\033[32m" + "You are staring at the dense trees," + "\033[0m")
    print("\033[32m" + "wondering how you will get by." + "\033[0m")
    print("\033[32m" + "The first thing you see is a signpost" + "\033[0m")
    print("\033[32m" + "that warn you about the many obstacles" + "\033[0m")
    print("\033[32m" + "you may meet inside and" + "\033[0m")
    print("\033[32m" + "that you have to overcome" + "\033[0m")
    print("\033[32m" + "them to continue on your journey." + "\033[0m")
    print("\033[32m" + "They will test your skills and" + "\033[0m")
    print("\033[32m" + "determination so you can get home." + "\033[0m")
    print("\033[32m" + "Take a deep breath," + "\033[0m")
    print("\033[32m" + "and let the adventure begin!" + "\033[0m")
 
    while True:
        choice = input("\033[32m" + "Are you ready? Type 'y' for" + "\033[0m")
        choice = input("\033[32m" + " yes or 'n' for no > " + "\033[0m")
        if choice == 'y':
            clearConsole()
            print("\033[32m" + "Here is some valid information about your character: \n Health: " + str(player_health) + "\n Attack: " + str(player_attack) + "\n Defense: " + str(player_defense) + "\033[0m")
            input("\033[32m" + "Press any key to enter the woods: " + "\033[0m")
            clearConsole()
            path_choice()
            break
        elif choice == 'n':
            print("\033[32m" + "Thanks for playing," + "\033[0m")
            print("\033[32m" + "have a good day!" + "\033[0m")
            game_over()
            break
        else:
            print("\033[31m" + "Invalid choice," + "\033[0m")
            print("\033[31m" + "type 'y' for yes or 'n' for no" + "\033[0m")
            clearConsole()
            continue


def path_choice():

    '''First path that leads the player to the next path'''

    print("\033[32mLets get started. Do you want to move forward?\033[0m")
    print("\033[32mType 'y' for yes and 'n' for no and quit game\033[0m")
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

    print("\033[35m" + "The air is damp and filled with" + "\033[0m")
    print("\033[35m" + "the scent of old trees" + "\033[0m")
    print("\033[35m" + "The rustling of leaves scared you a bit," + "\033[0m")
    print("\033[35m" + "anything could be hiding in the bushes" + "\033[0m")
    print("\033[35m" + "You get further in to the forest," + "\033[0m")
    print("\033[35m" + "there are tree logs laying everywhere." + "\033[0m")
    print("\033[35m" + "There's a big one" + "\033[0m")
    print("\033[35m" + "in the middle of the road," + "\033[0m")
    print("\033[35m" + "you have to climb over it to keep going" + "\033[0m")
    print("\033[35m" + "Type '1' for yes to climb the log or type" + "\033[0m")
    print("\033[35m" + "'2' to go another way." + "\033[0m")
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

    print("\033[35m" + "You can barely see anything now, the light that")
    print("\033[35m" + "once shined through the tree")
    print("tops is now a distant memory")
    print("\033[36m" + "You:\"This is the last time I leave my house,\"")
    print("\033[36m" + "\"it's just not worth it\"")
    print("\033[35m" + "You keep on walking, jumping over")
    print("\033[35m" + "the big branches streching over the pathway")
    print("\033[35m" + "You sense that you are not alone,")
    print("\033[35m" + "someone is watching you.")
    print("\033[35m" + "You stop in your tracks,")
    print("\033[35m" + "the smell of something rotten hits you!")
    print("\033[35m" + "Do you want to keep going?")
    print("Type 'y' for yes or 'n' for no and run away.\033[0m")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            player_encounter_goblin()
            break
        elif choice == 'n':
            clearConsole()
            print("\033[31mYou have no choice!\033[0m")
            player_encounter_goblin()
            break
        else:
            print("\033[31mInvalid choice, please type 'y' or 'r'\033[0m")
            continue


def path_choice_4():

    '''New path that introduces the player to an owl that will give them som
    inspiring words to keep on going + leads to meet the Witch'''

    print("\033[35mYou keep walking on what you think is the path,")
    print("\033[35myou are not sure.")
    print("It doesn't seem like anyone has been here for years")
    print("the roots of the trees are everywhere.")
    print("All of a sudden you see an old owl sitting on a branch.")
    print("It clears its throat and says:")
    print("\033[36m\"Hello there brave one,\"\033[0m")
    print("\033[36m\"I've been waiting for you!\"\033[0m")
    print("\033[36m\"To get to the end you must be even braver\"\033[0m")
    print("\033[36m\"hold on!\"\033[0m")
    print("\033[35mType 'l' to go left or 'f' to go forward")
    while True:
        choice = input("> \033[0m")
        if choice == 'l':
            clearConsole()
            meet_witch()
            break
        elif choice == 'f':
            print("\033[31mThe trees grow too dense here,\033[0m")
            print("\033[31myou can't get through\033[0m")
            print("\033[31mYou have to take another path\033[0m")
            print("\033[31mChoose 'l' to go left\033[0m")
            while True:
                choice = input("> ")
                if choice == 'l':
                    clearConsole()
                    meet_witch()
                    break
                else:
                    print("\033[1;31;40mInvalid choice,\033[0;37;40m")
                    print("\033[1;31;40mtype 'l' to keep going\033[0;37;40m")
                    continue
        else:
            print("\033[91mInvalid choice, please type 'l' or 'f'\033[0m")
            continue


def path_choice_5():

    '''
    The last path choice, here the player meet some forest gnomes
    This path leads to the Wizard.
    '''
    print("\033[35m" + "You move along, wondering what she meant")
    print("\033[35m" + "How many times will you rise and fall?")
    print("\033[35m" + "You study the the binders of")
    print("\033[35m" + "the book when all of a sudden")
    print("\033[35m" + "three small forest gnomes appear,")
    print("\033[35m" + "right in front of you")
    print("\033[36m" + "You: \"Hello, can I help you\"")
    print("\033[35m" + "The gnomes look at each other, and then back at you")
    print("\033[35m" + "Then all of them open their mouths")
    print("\033[35m" + "at the same time and say: ")
    print("\033[36m" + " \"You have to hurry, he is waiting for you\"")
    print("\033[36m" + "You:\"Huh, who is?\" ")
    print("\033[36m" + "Them:\"You will find out soon, just hurry!\"")
    print("\033[35m" + "They then grab each others hands and scurries off")
    print("\033[35m" + "You stand still for quick moment,")
    print("\033[35m" + "wondering what just happend")
    print("\033[35m" + "You then say to yourself: ")
    print("\033[36m" + "\"Well I cant stay here! I have to keep going\"")
    print("\033[35m" + "Do you want to continue?")
    print("\033[35m" + "type 'y' for yes and 'n' for no and end game")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            meet_wizard()
            break
        elif choice == 'n':
            clearConsole()
            game_over()
            break
        else:
            print("\033[91mInvalid choice, please type 'y' or 'n'\033[0m")
            continue


def riddle_encounter():

    '''Solve the riddle, gives different options + a valuable treasure'''

    riddles = ["What starts with an E, ends with an E,"]
    riddles = ["but only contains one letter?"]
    riddle = random.choice(riddles)
    print("\033[32mYou come across a treasure chest and a\033[0m")
    print("\033[32msign with a riddle written on it\033[0m")
    print("\033[32mto open the chest you must answer correctly!\033[0m")
    print("\033[32m" + riddle + "\033[0m")
    print("\033[32m1. Elephant\033[0m")
    print("\033[32m2. Envelope\033[0m")
    print("\033[32m3. Eagle\033[0m")
    print("\033[32m4. Edge\033[0m")
    while True:
        answer = input("\033[32mWhat is your answer?\033[0m ")
        if answer.lower() == "2":
            clearConsole()
            print("\033[32mCorrect! The chest is open!\033[0m")
            print("\033[32mYou collect the treasure inside!\033[0m")
            print("\033[32mThe treasure is shiny and heavy.\033[0m")
            print("\033[32mIt must be worth alot.\033[0m")
            print("\033[32mYou put it in your backpack\033[0m")
            print("\033[32mand start walking again.\033[0m")
            print("\033[32mDo you want to continue?\033[0m")
            print("\033[32mType '1' for yes or '2' for no\033[0m")
            while True:
                choice = input(">")
                if choice == '1':
                    clearConsole()
                    path_choice_2()
                    break
                elif choice == '1':
                    clearConsole()
                    game_over()
                    break
                else:
                    print("\033[31mInvalid choice, enter '1' or '2'\033[0m")
                    continue
            break
        else:
            print("\033[32mIncorrect. You have failed the task.\033[0m")
            game_over()


def player_encounter_goblin():

    '''Player meets the goblin/enemy'''

    goblin_health = 30
    goblin_attack = 5
    print("\033[31mYou have come across a nasty forest goblin!\033[0m")
    print("\033[31mDo you want to attack or run away?\033[0m")
    print("\033[31mEnter '1' to attack or '2' to run away!\033[0m")
    choice = input("\033[31m>\033[0m ")
    while goblin_health > 0:
        if choice == '1':
            global player_health
            player_attack = random.randint(10, 14)
            goblin_health -= player_attack
            if goblin_health <= 0:
                clearConsole()
                print("\033[32mYou have defeated the goblin!\033[0m")
                print("\033[32mYou may continue on your journey.\033[0m")
                print("\033[32mYou have received a 'Badge of Honor',\033[0m")
                print("\033[32monly brave ones get this.\033[0m")
                print("\033[32mDo you want to continue your journey?\033[0m")
                print("\033[32mEnter '1' for yes and \033[0m")
                print("\033[32m'2' for no and end game.\033[0m")
                while True:
                    choice = input("\033[32m>\033[0m ")
                    if choice == '1':
                        clearConsole()
                        meet_wizard()
                        break
                    elif choice == '2':
                        clearConsole()
                        game_over()
                        break
                    else:
                        print("\033[31mInvalid choice,enter '1' or '2'\033[0m")
                        clearConsole()
                        continue
            else:
                print("\033[31mThe goblin now has ")
                print("\033[31m" + str(goblin_health) + " health.\033[0m")
                player_health -= goblin_attack
            if player_health <= 0:
                game_over()
            else:
                print("\033[31mYou now have\033[0m")
                print("\033[31m" + str(player_health) + " health.\033[0m")        
                print("\033[31mDo you want to attack or run?\033[0m")
                print("\033[31mEnter '1' to attack and '2' to run.\033[0m")
                choice = input("\033[31m>\033[0m ")
        elif choice == '2':
            run_away_chance = random.randint(10, 14)
            if run_away_chance <= 70:
                clearConsole()
                print("\033[32mYou ran away from the goblin!\033[0m")
                print("\033[32mDo you want to continue your journey?\033[0m")
                print("\033[32mType 1 for yes and 2 for no ti end game\033[0m")
                while True:
                    choice = input("\033[32m>\033[0m ")
                    if choice == '1':
                        clearConsole()
                        meet_wizard()
                        break
                    elif choice == '2':
                        clearConsole()
                        game_over()
                        break
                    else:
                        print("\033[31mInvalid choice, type '1' or '2'\033[0m")
                        continue
                else:
                    print("\033[31mYou have\033[0m")
                    print("\033[31m" + str(player_health) + "health.\033[0m")
                    print("\033[31mDo you want to attack or run?\033[0m")
                    print("\033[31mEnter '1' to attack and '2' to run.\033[0m")
                    choice = input("\033[31m>\033[0m ")
        else:
            print("\033[31mInvalid choice, please type '1' or '2'\033[0m")
            choice = input("\033[31m>\033[0m ")


def meet_witch():
    '''
    Function that introduce the witch,
    here the player is given a book and an option to proceed to the Wizard
    '''
    print("\033[35mA beautiful Witch appears\033[0m")
    print("\033[35mWith a soft smile she says:")
    print("\033[36m\"Ah the wispers were right\" ")
    print("\033[36m\"There is a human here\" ")
    print("\033[36m\"I need to tell you something!\"")
    print("\"You ready? Okay, listen closely\"")
    print("\"The greatest glory in living lies not in never falling,\"")
    print("\"but in rising every time we fall\"")
    print("\"You need to remember this for the rest of your journey, okay\"?")
    print("\"Matter of fact, take this book,")
    print("\"it is filled with knowledge\"\033[0m")
    print("\033[35mYou have collected the book of wisdom.")
    print("\033[35mIt has been added to your inventory")
    print("\033[35mSuddenly the beautiful witch")
    print("\033[35mdisapears and you're all alone")
    print("\033[35mDo you want to continue your journey?")
    print("\033[35mEnter 'y' for yes or 'n' for no.")
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


def meet_wizard():
    '''
    A powerful Wizard who looks for his lost treasure,
    the player is given an option to give it to him or not
    '''
    print("\033[35mYou come across a wizard in the forest.")
    print("\033[35mHe looks at you and gasps:")
    print("\033[36m\"A human? In here?\"")
    print("\033[36m\"I havent seen any of your kind in a while\"")
    print("\"Well, most of you look like goblins,\"")
    print("\"but you don't smell as foul\"")
    print("\033[35m" + "He smirks at you." + "\033[0m")
    print("\033[36m\"I've been looking for my treasure for days!\"")
    print("\033[36m\"Have you seen it?\"")
    print("\033[35mYou remember the treasure you")
    print("\033[35mgot when you answered the riddle.")
    print("\033[35mIt seemed so valuable... ")
    print("\033[35mWhat would you like to do? ")
    print("\033[33m" + "1. Yes, here it is." + "\033[0m")
    print("\033[33m" + "2. No, I've never seen it." + "\033[0m")
    while True:
        choice = input("> ")
        if choice == '1':
            clearConsole()
            print("\033[35mThe Wizard says: ")
            print("\033[36m\"Ah, thank you! As a reward\"")
            print("\033[36m\"I will teleport you to the end of the forest.\"")
            print("\033[35m" + "Do you want to continue?")
            print("\033[35m" + "Enter '1' for yes or '2' for no.")
            while True:
                choice = input("> ")
                if choice == '1':
                    clearConsole()
                    complete_game()
                    break
                elif choice == '2':
                    clearConsole()
                    game_over()
                    break
                else:
                    print("\033[31mInvalid choice, please type '1' or '2'")
                    clearConsole()
                    continue
            break
        elif choice == '2':
            clearConsole()
            print("\033[36mWizard: \"Good luck getting over the stream\"")
            print("\033[36mWizard: \"over there by yourself, you bafoon!\"")
            print("\033[35mThe wizard grunts and vanish in a puff of smoke.")
            print("\033[35m" + "Do you want to continue?")
            print("\033[35m" + "Enter '1' for yes or '2' for no.")
            while True:
                choice = input("> ")
                if choice == '1':
                    clearConsole()
                    wild_stream()
                    break
                elif choice == '2':
                    clearConsole()
                    game_over()
                    break
                else:
                    print("\033[31mInvalid choice, please type '1' or '2'")
                    clearConsole()
                    continue
                break
        else:
            print("\033[31mInvalid choice, please type '1' or '2'")
            clearConsole()
            continue


def wild_stream():

    '''
    The last obstacle in  the game, this is were the player
    ends up if they don't help the wizard and give him his treasure.
    '''
    print("\033[31mYou come across a wild stream. What will you do?")
    print("1. Swim over")
    print("2. Jump over")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            print("\033[32mYou swim over the wild stream.")
            print("\033[32mand make it safely to the other side.")
            print("Type '1' to continue or '2' to end game")
            while True:
                choice = input("> ")
                if choice == '1':
                    clearConsole()
                    complete_game()
                    break
                elif choice == '2':
                    clearConsole()
                    game_over()
                    break
                else:
                    print("\033[31mInvalid choice, please type '1' or '2'")
                    continue
            clearConsole()
            complete_game()
            break
        elif choice == '2':
            print("\033[32mYou jump over the wild stream")
            print("\033[32mand make it safely to the other side.")
            clearConsole()
            complete_game()
            break
        else:
            print("\033[31mInvalid choice, please type '1' or '2'")
            continue


def complete_game():

    '''The game is finished and they have won.
    The player is greeted by some celebrating forest gnomes'''

    print("\033[32m" + "Light from the outside world shines through the trees")
    print("\033[32m" + "As you walk towards the end of the forest")
    print("\033[32m" + "a couple of forest gnomes greet you")
    print("\033[36m" + "\"You made it!! You're alive!!\"")
    print("\033[32m" + "They chant and dance in a cirkel around you")
    print("\033[36m" + "\"Well done, you made it to the other side.\"")
    print("\033[36m" + "\"Go home and rest, you deserve it!\"")
    print("\033[32m" + "Do you want to play again? (1. yes or 2. no)")
    while True:
        choice = input("> ")
        if choice == '1':
            clearConsole()
            start_game()
            break
        elif choice == '2':
            clearConsole()
            print("\033[32m" + "Thank you for playing! Welcome back anytime!")
            break
        else:
            print("\033[31mInvalid choice, please type '1' or '2'")
            continue


def game_over():

    ''' The player has died and the game is over,
    but they have options to try again if they want.'''

    print("\033[31m" + "This is where your story end, do you want to try again?")
    print("\033[32m" + "Enter 'y' for yes and 'n' for no and quit game")
    while True:
        choice = input("> ")
        if choice == 'y':
            clearConsole()
            start_game()
            break
        elif choice == 'n':
            print("\033[32m" + "Thank you for playing and welcome back!")
            clearConsole()
            break
        else:
            print("\033[31mInvalid choice, please type '1' or '2'")
            continue


start_game()