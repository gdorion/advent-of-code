#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import re

class Character(object):
    def __init__(self, name, damage, armor, hitpoints):
        self.name = name
        self.damage = int(damage)
        self.armor = int(armor)
        self.lifepoints = int(hitpoints)
        self.hitpoints = int(hitpoints)
        self.gear = []

    def __eq__(self, other):
        if isinstance(other, Character):
            return (self.name == other.name)
        return False

    def totalDamage(self):
        damage = self.damage
        for i in self.gear:
            damage += i.damage

        return damage

    def totalArmor(self):
        armor = self.armor
        for i in self.gear:
            armor += i.armor
        return armor

    def reset(self):
        self.hitpoints = self.lifepoints

    def gearCost(self):
        return sum(g.cost for g in self.gear)

    def hitBy(self, enemy):
        self.hitpoints -= max(1, (enemy.totalDamage() - self.totalArmor()))

class Item(object):
    def __init__(self, itemType, name, cost, damage, armor):
        self.itemType = itemType
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.name == other.name)
        return False

    def __repr__(self):
        return self.name


def play(player, boss):
    turn = True # Player is state 0 and always goes first

    while player.hitpoints > 0 and boss.hitpoints > 0:
        if turn:
            boss.hitBy(player)
        else:
            player.hitBy(boss)

        turn = not turn

    if boss.hitpoints <= 0 and player.hitpoints > 0:
        return True

    return False


# Init items and characters data
player  = Character('player', 0, 0, 100)
boss    = Character('boss', 8, 2, 100)
initial = open('data.txt').read().splitlines()
weapons = []
armors = []
rings = []

for i, l in enumerate(initial):
    itemParams = re.findall('([\w]+)', l)
    item = Item(itemParams[0],itemParams[1],itemParams[2],itemParams[3], itemParams[4])
    if item.itemType == 'Weapon':
        weapons.append(item)
    elif item.itemType == 'Armor':
        armors.append(item)
    else:
        rings.append(item)

# Generate all gear possibilities
gearSet = []
for w in weapons:
    for a in armors:
        for r in rings:
            for r2 in rings:
                if r != r2:
                    gear = [w,a,r,r2]
                    gearSet.append(gear)

#Part 1
minCost = 999
maxCost = 0

for gs in gearSet:
    player.gear = gs
    player.reset()
    boss.reset()

    if play(player, boss) :
        minCost = min(minCost, player.gearCost())
    else:
        maxCost = max(maxCost, player.gearCost())

print minCost
print maxCost
