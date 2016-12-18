#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
# Remarks : Ported code from zelos :http://pastebin.com/ciHCcvfi (C++)
#           in python to compare speeds with previous algorithm.
#

bosshp = 58
spellcost = [53,73,113,173,229]
bossdam = 9

best = 99999

def play(bosshp, playerhp, mana, cost, spellshield, spellpoison, spellrecharge, spell):
    global spellcost, best, bossdam

    # Player
    if spell == 0:
        bosshp -= 4

    if spell == 1:
        playerhp+=2
        bosshp -=2

    if spell == 2:
        if spellshield == 0:
            spellshield = 6
        else:
            return False

    if spell == 3:
        if spellpoison == 0:
            spellpoison = 6
        else:
            return False

    if spell == 4:
        if (spellrecharge == 0):
            spellrecharge = 5
        else:
            return False

    mana -= spellcost[spell]
    cost += spellcost[spell]

    if bosshp <= 0:
        if cost < best:
            best = cost
        return True

    #Boss
    if spellrecharge > 0:
        mana += 101
        spellrecharge-=1

    if spellpoison > 0:
        bosshp -= 3
        spellpoison-=1

    if spellshield > 0:
        spellshield -= 1
        armor = 7
    else:
        armor = 0

    if bosshp > 0:
        if ((bossdam - armor ) < 1):
            playerhp -= 1
        else:
            playerhp -= (bossdam - armor)
    else:
        if (cost < best):
            best = cost
        return True

    playerhp-=1  # hard mode bleed effect
    if playerhp <= 0:
        return False

    # player turn begin
    if (spellshield > 0):
        spellshield -= 1

    if (spellrecharge > 0):
        mana += 101
        spellrecharge -= 1

    if (spellpoison > 0):
        bosshp -= 3
        spellpoison -= 1

    if (bosshp <= 0):
        if (cost < best):
            best = cost
        return True


    for nextspell in range(0, 5):
        if (mana >= spellcost[nextspell]):
            play(bosshp, playerhp, mana, cost, spellshield, spellpoison, spellrecharge, nextspell)

    return False

for firstspell in reversed(range(4)): # From part 1 the best score was in the third node so we search from there right aways.
    print ("(%d) " % (firstspell))
    play(bosshp, 49, 500, 0, 0, 0, 0, firstspell)
    print best

