from hero import Hero
import random
# from func import d
hero = Hero('josh')


def d(num):
    random_num = random.randint(1, num)
    return random_num


class Monster:

    def __init__(self, name, desc, speed, dexterity, strength, constitution, intelligence, monster_hp, attacks, loot):
        self.name = name
        self.desc = desc
        self.speed = speed
        self.dexterity = dexterity
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.monster_hp = monster_hp
        self.attacks = attacks
        self.loot = loot


rat = Monster(
    name='rat',
    desc=[
        'a big hairy rat',  # introduce monster
        '',
        '',
        '',
        '  ( )( )--.',
        '    \\../ (  )',
        "       m\\/m--m'`--.",
        '',
        '',
        '',
        ''
    ],
    speed=1,
    dexterity=1,
    strength=1,
    constitution=1,
    intelligence=1,
    monster_hp=9,
    attacks={
        # attack name: damage range
        'scratch': d(4)
    },
    loot={
        # for x in monster.loot.keys():
        #   if random.randint(1,100) <= monster.loot[x]
        #       add to hero.inventory
        'gold': [random.randint(1, 3), 100],
        'potion': [1, 100],
        'herb': [1, 10]
    }
    )


# test how monsters are displaying
def monster_test(monster):
    print('----------------------------------------------------------')
    print(('{}     {}'.format(('-' * 50), 'character stats:')))
    print('{:<8s} {:^30s} hp-{:<6} {:>1s}'.format('|', monster.desc[0], str(monster.monster_hp), '|',))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[1], '|',))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[2], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[3], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[4], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[5], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[6], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[7], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[8], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[9], '|'))
    print('{:<1s} {:^47s} {:>1s}'.format('|', monster.desc[10], '|'))
    print(('-' * 50))





def loot_monster(monster):
    # stores the loot dropped by this specific mob and displays a victory message with loot
    temp_loot = {}
    for loot in monster.loot.keys():
        if random.randint(1, 100) <= monster.loot[loot][1]:
            hero.inventory[loot] += rat.loot[loot][0]
            temp_loot[loot] = rat.loot[loot][0]
    for item in hero.inventory.keys():
        if hero.inventory[item] > 0:
            hero.inventory_to_display[item] = hero.inventory[item]
    print('\nYou defeated the {} and obtained the following:'.format(monster.name))
    for z in temp_loot.keys():
        print('{} - {}'.format(z, temp_loot[z]))




# monster_test(rat)
# loot_monster(rat)
# for x in hero.inventory_to_display:
#     print('{} - {}'.format(x, hero.inventory_to_display[x]))
