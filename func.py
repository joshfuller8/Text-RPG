from rooms import *
import random

current_location = xx
previous_location = xx
hero = Hero('josh')


def check_player_input(current_location, previous_location):
    """displays choices for the player in this room and verifies their input
    if the input is valid, then the player is moved to that room

    :param current_location: current room that the player is in
    :param previous_location: room that the player was last in
    :return: None
    """

    while True:
        previous_location = current_location
        print('\nYou can choose from the following directions:\n')
        for n in current_location.exits.keys():
            print(n)
        print()
        player_input = input('What would you like to do?: ')
        for word in player_input.split(' '):
            if word == 'quit':
                quit()
            if word in current_location.exits.keys():
                current_location = rooms[current_location.exits[word]]
                break
            else:
                print('\nyou cannot do that\n')
                continue
        break


def check_player_stats():
    """checks to see if a player has died and adjusts hp/mp totals so that a player
    does not have more hp/mp than their max

    :return: None
    """
    if hero.current_hp >= hero.calc_max_hp():
        hero.current_hp = hero.calc_max_hp()
    if hero.current_mp >= hero.max_mp:
        hero.current_mp = hero.max_mp
    if hero.current_hp <= 0:
        print('GAME OVER')
        quit()
    if hero.current_mp <= 0:
        hero.current_mp = 0


def d(num):
    """Used to simulate a dice roll.

    :param num: takes a positive integer
    :return: returns a random integer between 1 and num
    """
    random_num = random.randint(1, num)
    return random_num


def display_exits(current_location):
    """Displays a list of available choices for the player

    :param current_location: current room that the player is in
    :return: None
    """

    current_location.available_exits = {}
    exit_names = []
    exit_counter = 1
    for x in current_location.exits.keys():
        current_location.available_exits[exit_counter] = x
        exit_names.append('{}. {}'.format(exit_counter, x))
        exit_counter += 1
    try:
        exit_names[0] = exit_names[0]
    except IndexError:
        exit_names.append('')
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


def display_room(current_location):
    """Basic display for the player to see where they are. Includes
    current hp/mp, inventory, room

    :param current_location: current room that the player is in
    :return: None
    """

    loc = current_location
    if hero.inventory['potion'] <= 0:
        potion = ''
        potion_value = ''
    else:
        potion = 'potion -'
        potion_value = hero.inventory['potion']
    # This is the displayed room, each line is a part of a square display for the player UI
    print('--------------------------------------------------------------------------------')
    print(('{} {}        {}'.format(('-' * 50), loc.name, 'character stats:')))
    print('{:<1s} {:^47s} {:>1s} {:>17} {:>1}/{:>1}'.format('|', loc.desc[0],
                                                            '|',
                                                            'hp -',
                                                            hero.current_hp,
                                                            hero.calc_max_hp()))
    print('{:<1s} {:^47s} {:>1s} {:>17} {:>1}'.format('|', loc.desc[1],
                                                      '|',
                                                      'mp -',
                                                      hero.current_mp))
    print('{:<1s} {:^47s} {:>1s} {:>17} {:>1}'.format('|', loc.desc[2], '|', 'gold -',
                                                      hero.inventory['gold']))
    print('{:<1s} {:^47s} {:>1s} {:>17} {:>1}'.format('|', loc.desc[3], '|', potion,
                                                      potion_value))
    print('{:<1s} {:^47s} {:>1s}'.format('|', loc.desc[4], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', loc.desc[5], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', loc.desc[6], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', loc.desc[7], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', loc.desc[8], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', '', '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', '', '|'))
    print(('-' * 50))


def encounter_check(current_location, previous_location):
    if previous_location.name != current_location.name:
        encounter_roll = random.randint(1, 100)
        if encounter_roll <= current_location.encounter_chance:
            # table_roll is the number that will be associated on the encounter table
            table_roll = random.randint(1, 2)
            monster = current_location.encounter_table[table_roll]
            random_encounter(monster)


def enter_to_continue():
    press_enter = input('\nPress ENTER to continue: ')
    if press_enter == '':
        pass


def random_encounter(monster):
    monster_alive = True
    turn_count = 1
    potion = ''
    if hero.inventory['potion'] <= 0:
        potion = ''
        potion_value = ''
    else:
        potion = 'potion -'
        potion_value = hero.inventory['potion']
    monster_hp = monster.monster_hp
    if random.randint(1, 21) + hero.speed >= random.randint(1, 21) + monster.speed:
        active_player = 'hero'
    else:
        active_player = 'monster'
    while monster_alive:
        while active_player == 'monster':
            attack = random.choice(list(monster.attacks.keys()))
            damage = monster.attacks[attack]
            hero.current_hp -= damage
            active_player = 'hero'
            monster_text1 = 'the {} used {} and'.format(monster.name, attack)
            monster_text2 = 'dealt {} damage!'.format(damage)
            # use display_monster() instead of the large block below
            print('------------------------------------------------------------------------------------------------')
            if turn_count == 1:
                print('The {} attacked first!'.format(monster.name))
            print(('{}     {}'.format(('-' * 50), 'character stats:')))
            print('{:<8s} {:^30s} hp-{:<6} {:>1s} {:>10} {:>1}/{:>1}'.format('|', monster.desc[0], str(monster_hp),
                                                                             '|',
                                                                             'hp -',
                                                                             hero.current_hp,
                                                                             hero.calc_max_hp()))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[1],
                                                              '|',
                                                              'mp -',
                                                              hero.current_mp))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[2], '|', 'gold -',
                                                              hero.inventory['gold']))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[2], '|', potion,
                                                              potion_value))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[4], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[5], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[6], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[7], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[8], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster_text1, '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster_text2, '|'))
            print(('-' * 50))
            check_player_stats()
            # # blank line to separate the display
            # print('The {} used {} and dealt {} damage'.format(monster.name, attack, damage))
            turn_count += 1
            # enter_to_continue()

        # player's turn
        while active_player == 'hero':
            if turn_count == 1:
                print(
                    '------------------------------------------------------------------------------------------------')
                print('your move first!')
                print(('{}     {}'.format(('-' * 50), 'character stats:')))
                print('{:<8s} {:^30s} hp-{:<6} {:>1s} {:>10} {:>1}/{:>1}'.format('|', monster.desc[0], str(monster_hp),
                                                                                 '|',
                                                                                 'hp -',
                                                                                 hero.current_hp,
                                                                                 hero.calc_max_hp()))
                print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[1],
                                                                  '|',
                                                                  'mp -',
                                                                  hero.current_mp))
                print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[2], '|', 'gold -',
                                                                  hero.inventory['gold']))
                print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[3], '|', potion,
                                                                  potion_value))
                print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[4], '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[5], '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[6], '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[7], '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[8], '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', '', '|'))
                print('{:<1s} {:^47s} {:>1s}'.format('|', '', '|'))
                print(('-' * 50))
            hero_text1 = ''
            hero_text2 = ''
            battle_command = input('\n what would you like to do? ')

            if battle_command == 'kill':
                monster_alive = False
                break
            elif battle_command == 'attack':
                h_damage = hero.attack
                hero_text1 = 'You swing your sword at the {}'.format(monster.name)
                hero_text2 = 'and deal {} damage!'.format(h_damage)
                monster_hp -= h_damage
                active_player = 'monster'
                turn_count += 1
                if monster_hp <= 0:
                    loot_monster(monster)
                    monster_alive = False
                    enter_to_continue()
                    break
            else:
                print('try another command')
            # same thing as above
            print('------------------------------------------------------------------------------------------------')
            print(('{}     {}'.format(('-' * 50), 'character stats:')))
            print('{:<8s} {:^30s} hp-{:<6} {:>1s} {:>10} {:>1}/{:>1}'.format('|', monster.desc[0], str(monster_hp),
                                                                             '|',
                                                                             'hp -',
                                                                             hero.current_hp,
                                                                             hero.calc_max_hp()))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[1],
                                                              '|',
                                                              'mp -',
                                                              hero.current_mp))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[2], '|', 'gold -',
                                                              hero.inventory['gold']))
            print('{:<1s} {:^47s} {:>1s} {:>10} {:>1}'.format('|', monster.desc[3], '|', potion,
                                                              potion_value))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[4], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[5], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[6], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[7], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[8], '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', hero_text1, '|'))
            print('{:<1s} {:^47s} {:>1s}'.format('|', hero_text2, '|'))
            print(('-' * 50))
            enter_to_continue()
            # bLANK LINE SEPARATOR


# not currently being used


# random_encounter(rat)
# # loot_monster(rat)
# # print('\nYou defeated the {} and obtained the following:'.format(rat.name))
# # for x in hero.inventory_to_display:
# #     print('{} - {}'.format(x, hero.inventory_to_display[x]))
# enter_to_continue()
# random_encounter(rat)
