#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import copy
import random

buffs = ['Shield', 'Poison', 'Recharge']

class Effect(object):
    def __init__(self, nbTurns, damage, healing, armor, manaRecharge):
        self.nbTurns = int(nbTurns)
        self.remainingTurns = 0
        self.damage = int(damage)
        self.healing = int(healing)
        self.armor = int(armor)
        self.manaRecharge = int(manaRecharge)

class Spell(object):
    def __init__(self,name, effect,  cost):
        self.name = name
        self.cost= int(cost)
        self.effect = effect

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        if isinstance(other, Spell):
            return (self.name == other.name)
        return False

    def __repr__(self):
        return '%s(%d)' % (self.name, self.effect.remainingTurns)

class Character(object):
    def __init__(self, name, damage, hitpoints, manaPoints):
        self.name = name
        self.damage = int(damage)
        self.armor = 0
        self.manaPoints = int(manaPoints)
        self.hitpoints = int(hitpoints)

        self.remainingMana = int(manaPoints)
        self.lifepoints = int(hitpoints)

        self.spellSet = []
        self.ongoingSpells = []
        self.manaSpent = 0

    def __eq__(self, other):
        if isinstance(other, Character):
            return (self.name == other.name)
        return False

    def reset(self):
        self.remainingMana = self.manaPoints
        self.hitpoints = self.lifepoints
        self.nextSpellIndex = 0
        self.spellSet = []
        self.armor = 0

        for s in self.ongoingSpells:
            s.effect.remainingTurns = 0

    def processOngoingSpells(self):
        for s in self.ongoingSpells:
            if s.effect.remainingTurns > 0:
                castSpell(s, self, self)

    def hit(self, enemy):
        enemy.hitpoints -= max(1, self.damage - enemy.armor)

def castSpell(spell, attacker, enemy):
    if enemy.name == 'Boss':
        enemy.hitpoints        -= spell.effect.damage
    if attacker.name == 'Player':
        attacker.remainingMana = min(attacker.remainingMana + spell.effect.manaRecharge, attacker.manaPoints)
        attacker.hitpoints     = min(attacker.hitpoints + spell.effect.healing, attacker.lifepoints)
        attacker.armor         = max(spell.effect.armor, attacker.armor)

    spell.effect.remainingTurns = max(spell.effect.remainingTurns - 1, 0)

def startSpell(spell, attacker, target):
    if spell.name == 'Poison':
        for s in target.ongoingSpells:
            if s.name == spell.name:
                s.effect.remainingTurns = s.effect.nbTurns # Assume spell was cast at least once before effect takes place
    else:
        for s in attacker.ongoingSpells:
            if s.name == spell.name:
                s.effect.remainingTurns = s.effect.nbTurns

def nextSpell(spells, manaRemaining):
    possibleSpells = []
    for s in spells:
        if s.cost <= manaRemaining:
            possibleSpells.append(s)

    if len(possibleSpells) > 0:
        return possibleSpells[random.randrange(0, len(possibleSpells))]
    return None

def play(player, boss, spells):
    global buffs
    turn = True # Player is state 0 and always goes first
    minCost = 99999999

    for i in range(1000000):
        player.reset()
        boss.reset()
        boss.ongoingSpells = copy.deepcopy(spells)
        player.ongoingSpells = copy.deepcopy(spells)
        index = 0

        while player.hitpoints > 0 and boss.hitpoints > 0 and player.remainingMana > 0:
            armor = 0
            player.processOngoingSpells()
            boss.processOngoingSpells()

            if turn:
                #test1
                #spellSet = [Spell('Poison', Effect(6,3,0,0,0), 173), Spell('MagicMissile', Effect(1,4,0,0,0), 53)]

                #test2
                #spellSet = [Spell('Recharge', Effect(5,0,0,0,101), 229), Spell('Shield', Effect(6,0,0,7,0), 113), Spell('Drain', Effect(1,2,2,0,0), 73), Spell('Poison', Effect(6,3,0,0,0), 173), Spell('MagicMissile', Effect(1,4,0,0,0), 53)]
                #spell = copy.deepcopy(spellSet[index])

                #puzzle
                spell = nextSpell(spells, player.remainingMana)

                if spell == None:
                    break

                player.spellSet.append(spell)
                if len(player.spellSet) > 5:
                    break

                if spell.name in buffs:
                    startSpell(spell, player, boss)
                else:
                    castSpell(spell, player, boss)

                player.manaSpent += spell.cost

                #print('Using spell:' + spell.name)
                player.remainingMana = max(0, player.remainingMana - spell.cost)
                index += 1

            else:
                boss.hit(player)
                #print('Boss hits')

            #print('Player:[HP:%s,Mana:%s,Armor:%s] Boss:%s' % (str(player.hitpoints), str(player.remainingMana), str(player.armor), str(boss.hitpoints)))
            turn = not turn

        if boss.hitpoints <= 0:
            if player.manaSpent < minCost:
                minCost = player.manaSpent
                print minCost

    return minCost


# Init items and characters data

#test1
#player  = Character('Player', 0, 10, 250)
#boss    = Character('Boss', 8, 13, 0)

#test2
player  = Character('Player', 0, 10, 250)
boss    = Character('Boss', 8, 14, 0)

#Puzzle input
#player  = Character('Player', 0, 50, 500)
#boss    = Character('Boss', 9, 58, 0)

spells = [
    Spell('MagicMissile', Effect(1,4,0,0,0), 53),
    Spell('Drain', Effect(1,2,2,0,0), 73),
    Spell('Shield', Effect(6,0,0,7,0), 113),
    Spell('Poison', Effect(6,3,0,0,0), 173),
    Spell('Recharge', Effect(5,0,0,0,101), 229),
]

play(player, boss, spells)

