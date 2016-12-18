#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

class Ingredients(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

ingredients = []
total = 100

with open('data.txt') as f:
    for line in f:
        l = line.rstrip('\n')
        l = l.replace(':','')
        l = l.replace(',','')

        params = l.split('.')[0].split(' ')
        ingredients.append(Ingredients(params[0], params[2], params[4], params[6], params[8], params[10]))

results = []
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            for l in range(1, 101):
                if i + j + k + l  == 100:
                    results.append([i, j, k, l])

params = [0,0,0,0]
scores = []
for r in results:
    params[0] = max(0, (r[0] * ingredients[0].capacity) + (r[1] * ingredients[1].capacity) + (r[2] * ingredients[2].capacity) + (r[3] * ingredients[3].capacity))
    params[1] = max(0, (r[0] * ingredients[0].durability) + (r[1] * ingredients[1].durability) + (r[2] * ingredients[2].durability) + (r[3] * ingredients[3].durability))
    params[2] = max(0, (r[0] * ingredients[0].flavor) + (r[1] * ingredients[1].flavor) + (r[2] * ingredients[2].flavor) + (r[3] * ingredients[3].flavor))
    params[3] = max(0, (r[0] * ingredients[0].texture) + (r[1] * ingredients[1].texture) + (r[2] * ingredients[2].texture) + (r[3] * ingredients[3].texture))

    scores.append(params[0] * params[1] * params[2] * params[3])

#print scores
print max(scores)
