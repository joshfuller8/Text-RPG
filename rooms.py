from monsters import *


class Room:

    def __init__(self, name, exits, available_exits, description, encounter_chance, encounter_table, secrets):
        # name must be a string
        self.name = name
        # exits must be a dictionary in format of choice: destination (destination must be a string)
        self.exits = exits
        # description of the room in centered lines
        self.desc = description
        # chance of having a random encounter on a d100 in this room
        self.encounter_chance = encounter_chance
        # dictionary of possible monsters in format num: monster
        self.encounter_table = encounter_table
        self.secrets = secrets
        self.available_exits = available_exits


# room template
nn = Room(
    name='',
    exits={
        # format is 'direction': 'room name as a string'
     },
    available_exits={},
    description=[
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
        ],
    encounter_chance=0,
    encounter_table={
        # num to roll: monster ie. rat
        1: 'monster',
        2: 'monster',
        3: 'monster',
        4: 'monster',
        5: 'monster',
        6: 'monster',
        7: 'monster',
        8: 'monster',
        9: 'monster',
        10: 'monster'
    },
    secrets={
        # format is 'secret trigger word': ['perception check', 'exit name', 'text to display']
    }
    )


# this room is only used for the intro, players will start in room xx
prologue = Room(
    name='  ',
    exits={},
    available_exits={},
    description=[
        'You awake in a dense forest',
        'you have no memory of what happened',
        'or where to go from here',
        '',
        'You pick up the sword lying on the ground',
        'and ponder what to do...',
        '',
        '',
        '',
        '',
        ''
    ],
    encounter_chance=0,
    encounter_table={},
    secrets=[]
)
# this is the starting square aka center
xx = Room(
    name='xx',
    exits={'north': 'a1', 'south': 'c1', 'east': 'b1', 'west': 'd1'},
    available_exits={},
    description=[
        'You are standing where you woke up,',
        'in all directions, you see nothing but trees.',
        '',
        'There is nothing of interest here',
        '',
        'You must pick a direction',
        'and start walking',
        '',
        '',
        '',
        ''
    ],
    encounter_chance=0,
    encounter_table={},
    secrets={
        'rock': [100, 'secret exit', 'r1', 'you found a secret']
    }
)

a1 = Room(
    name='a1',
    exits={'south': 'xx'},
    available_exits={},
    description=[
        '',
        'You are still in the forest',
        '',
        'there is nothing of note here',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ],
    encounter_chance=100,
    encounter_table={
        1: rat,
        2: rat,
        3: rat,
        4: rat,
        5: rat,
        6: rat,
        7: rat,
        8: rat,
        9: rat,
        10: rat
    },
    secrets=[]
)

b1 = Room(
    name='b1',
    exits={},
    available_exits={},
    description=[
        '',
        'this is b1',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '10',
        ''
        ],
    encounter_chance=0,
    encounter_table={},
    secrets=[]
    # secrets is a dictionary containing keys that lead to functions
    )

r1 = Room(
    name='b1',
    exits={},
    available_exits={},
    description=[
        '',
        'this is b1',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '10',
        ''
    ],
    encounter_chance=0,
    encounter_table={},
    secrets=[]
    # secrets is a dictionary containing keys that lead to functions
)


# this dictionary is necessary to convert string to object
# format is rooms[current_location.exits[word]] to get the object destination, word come from player_input.split()
# this needs to contain every room in the game, going to be very long
rooms = {
    'xx': xx,
    'a1': a1,
    'b1': b1,
    'r1': r1
}

previous_location = xx
current_location = xx