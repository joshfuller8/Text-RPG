from hero import Hero
hero = Hero('mike')
from monsters import *
from rooms import *


# monster = Monster(rat)
# Challenge time!
# We have mentioned that the data for the Adventure game could be organised in many
# different ways.  We've created another way for you.
# Your mission, if you choose to accept it, is to
# change the code to make it work.
# Below is the the complete program from the last video, but with the
# locations dictionary modified so that everything is in a single dictionary.
# N.B. Yes the code has some errors, thats what you need to fix!

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(locati.keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#     else:
#         allExits = exits[loc].copy()
#         allExits.update(namedExits[loc])
#
#     direction = input("Available exits are " + availableExits).upper()
#     print()
#
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:  # more than 1 letter, so check vocab
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:   # does it contain a word we know?
#                 direction = vocabulary[word]
#                 break
#
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")
#
from func import Room


def check_player_stats():
    if hero.current_hp >= hero.max_hp:
        hero.current_hp = hero.max_hp
    if hero.current_mp >= hero.max_mp:
        hero.current_mp = hero.max_mp
    if hero.current_hp <= 0:
        print('GAME OVER')
        quit()
    if hero.current_mp <= 0:
        hero.current_mp = 0


def d(num):
    random_num = random.randint(1, num)
    return random_num


# f = d(20)
# print(d(20))
# print(d(20))


# print(d(4) + d(4))







current_location = xx



# create a list of available exits with a number associated to them
# display those exits like this    1. exit1    2. exit2      3. exit3
# be able to append secret exits and have them not error out
# this should work off current_location.exits regardless of size
def display_exits(current_location):
    current_location.available_exits = {}
    exit_names = []
    exit_counter = 1
    for x in current_location.exits.keys():
        current_location.available_exits[exit_counter] = x
        exit_names.append('{}. {}'.format(exit_counter, x))
        exit_counter += 1
    try:
        exit_names[1] = exit_names[1]
    except IndexError:
        exit_names.append('')
    try:
        exit_names[2] = exit_names[2]
    except IndexError:
        exit_names.append('')
    try:
        exit_names[3] = exit_names[3]
    except IndexError:
        exit_names.append('')
    try:
        exit_names[4] = exit_names[4]
    except IndexError:
        exit_names.append('')
    try:
        exit_names[5] = exit_names[5]
    except IndexError:
        exit_names.append('')
    print('\n{:<1} {:>12} {:>12}'.format(exit_names[0], exit_names[1], exit_names[2]))
    print('{:<1} {:>12} {:>12}'.format(exit_names[3], exit_names[4], exit_names[5]))
    # these print the number associated with the exit (0) at position in exit_names
    # print(exit_names[0][0])
    # print(exit_names[1][0])

# current_location.exits['rock'] = 'a1'
# display_exits(current_location)


# inp = input(' :')
# if int(inp) == 2:
#     print(int(inp))
# else:
#     print('no')


# def rebuy(num):
#     # points = [.27, .265, .26, .255, .25, .245, .24, .235, .23, .225, .22, .215, .21, .205, .20, .19, .18, .17, .16,]
#     price = .0001
#     while price < .6:
#         shares_to_buy = round(((num - 20) // price), 3)
#         print(' {}  -  {} shares'.format(str(price).lstrip('0'), shares_to_buy))
#         price += .0001
#         price = round(price, 4)
#
#
# rebuy(550)


