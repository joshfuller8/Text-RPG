import random


def d(num):
    """Used to simulate a dice roll.

    :param num: takes a positive integer
    :return: returns a random integer between 1 and num
    """
    random_num = random.randint(1, num)
    return random_num


class Hero:
    hp_modifier = 0

    max_mp = 10
    current_hp = 20
    current_mp = 10
    dexterity = 3
    constitution = 3
    strength = 3
    intelligence = 3
    speed = 3
    attack = d(4) + strength
    battle_actions = {
        # format is 'action': [damage, 'hero_text1', 'hero_text2']
        # 'attack': [d(4) + strength, 'You swing your sword at the {}'.format(monster.name),
        #           'and deal {} damage!'.format(h_damage)]
    }
    inventory = {
        'gold': 10,
        'potion': 0,
        'herb': 0
    }
    inventory_to_display = {}

    def __init__(self, name):
        self.name = name

    def calc_max_hp(self):
        return 10 + (self.constitution * 5) + self.hp_modifier

    # this does not allow manual assignment of new max hp via +=
    # def max_hp(self, constitution):
    #     print(10 + (9 * constitution))
    #
    # def max_mp(self, intelligence):
    #     return 8 + (6 * intelligence)


# hero = Hero('john')
# print(hero.max_hp)   # 37
#
# hero.constitution = 4
# hero.max_hp(hero.constitution)
# print(hero.constitution)
# hero.max_hp += 11
# print(hero.max_hp)
#
# hero.constitution += 1
# print(hero.max_hp)
# hero.max_hp(hero.constitution)

#
# print(hero.calc_max_hp())
# hero.hp_modifier += 9
# print(hero.calc_max_hp())
# print(hero.hp_modifier)
