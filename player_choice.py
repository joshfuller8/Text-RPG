# take input from player
# determine if input is a valid exit choice
# if valid, set chosen_exit to the exit specified
# otherwise, redisplay the room with no random encounter
# this means that randomencounter needs to be a seprate func that is executed
# before a room is displayed

from rooms import *


def check_player_input():
    global current_location
    global previous_location
    while True:
        print('\nYou can choose from the following directions:\n')
        for x in current_location.exits.keys():
            print(x)
        print()
        player_input = input('What would you like to do?: ')
        for word in player_input.split(' '):
            if word == 'quit':
                game_on = False
            if word in current_location.exits.keys():
                previous_location = current_location
                current_location = rooms[current_location.exits[word]]
                break
            else:
                print('\nyou cannot do that\n')
                continue
        break
