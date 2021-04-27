from func import display_room, encounter_check, display_exits
from rooms import *


if __name__ == "__main__":
    # welcome message explaining the game
    print('*' * 50)
    print('\nWelcome to the game')
    print('enter commands like "north" or "go south" to move around the map')
    print('some areas may have secret commands, some may not')
    print('choose a listed exit to move to the next area')
    print('or try entering commands like "climb tree" and see what happens')
    print('\nbut most importantly....')
    print('\nhave fun\n')
    print('*' * 50)
    print("\nlet's get started!\n")
    # ask for hero name
    hero = Hero(input('What is your name?: '))
    print()
    # welcome the player
    print('Welcome {}'.format(hero.name.capitalize()))
    display_room(current_location=prologue)
    end_prologue = input('\npress ENTER to continue: ')
    game_on = True
    global previous_location
    global current_location
    # this is the game
    secret_phrases = []
    while game_on:
        # check for encounter before displaying the room
        encounter_check(current_location, previous_location)
        # display the first room
        display_room(current_location)
        # display the available exits, check input and change loc if correct
        # below is check_player_input(), but it is not working, so it is typed out instead
        # secret_triggered = False

        while True:
            previous_location = current_location
            # secret_triggered = False    probably wrong spot
                # secret_phrases.append(current_location.secrets[word][3] is the phrase

            # for x in current_location.exits.keys():
            #     print(x)
            if len(secret_phrases) >= 1:
                for phrase in secret_phrases:
                    print(phrase)
                secret_phrases = []
            print('\nYou can choose from the following directions:')
            display_exits(current_location)

            # secret_triggered = False
            print()
            player_input = input('What would you like to do?: ')
            # reset point
            # allows players to input displayed numbers as choices
            if len(player_input) == 1:
                if int(player_input) in current_location.available_exits.keys():
                    current_location = rooms[current_location.exits[
                        current_location.available_exits[int(player_input)]]]
                    break
            # reset point ^
            for word in player_input.split(' '):
                if word == 'quit':
                    game_on = False
                if word in current_location.exits.keys():
                    current_location = rooms[current_location.exits[word]]
                    break
                elif word in current_location.secrets.keys():
                    current_location.exits[current_location.secrets[word][1]] = current_location.secrets[word][2]
                    secret_phrases.append(current_location.secrets[word][3])
                    secret_triggered = True
                    print('trigger')
                    break
                else:
                    print('\nyou cannot do that\n')
                    continue
            break
        # end of check_player_input()
       # check_player_input(current_location, previous_location)