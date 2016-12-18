#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

class Reindeer(object):
    def __init__(self, name, speed, flightTime, restTime):
        self.name = name
        self.speed = speed
        self.flightTime = flightTime
        self.restTime = restTime

        # Results
        self.timeFlying = 0
        self.distance = 0
        self.points = 0

    def takeAction(self, iteration, duration):
        if self.isFlying(iteration, duration):
            self.distance = self.distance + self.speed
            return True

    def isFlying(self, iteration, duration):
        if (iteration % (self.flightTime + self.restTime)) < self.flightTime:
            return True
        return False

reindeers = []
dt = 2503

def findLeader(reindeers):
    best = 0
    for r in reindeers:
        if r.distance >= best:
            best = r.distance

    for r in reindeers:
        if r.distance == best:
            r.points = r.points + 1

with open('data.txt') as f:
    for line in f:
        l = line.rstrip('\n')
        params = l.split('.')[0].split(' ')

        # Set the speed all on a km/s base
        reindeers.append(Reindeer(params[0], int(params[3]), int(params[6]), int(params[13])))

for second in range(dt):
    for reindeer in reindeers:
        reindeer.takeAction(second, dt)
    findLeader(reindeers)

longest = 0
for reindeer in reindeers:
    print reindeer.name + " " + str(reindeer.distance) + "(%s)" % (str(reindeer.points))


winner = reindeers[0]
for reindeer in reindeers:
    if winner.points < reindeer.points:
        winner = reindeer

print winner.name + ' ' + str(winner.distance)  + ' ' + str(winner.points)



