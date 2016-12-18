#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
import math

class Point(object):
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __repr__(self):
        return str(self)
    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)
    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y


class Trail(object):
    def __init__(self, name, originX, originY):
        self.trail = []
        self.name = name
        self.origin = Point(originX, originY)
        self.extend(self.origin)

    def __repr__(self):
        return self.name + str(self.trail)

    def move_left(self):
        print "origin before" + str(self.origin)
        self.origin.X = self.origin.X - 1
        print "origin after" + str(self.origin)
        self.extend(self.origin)
        return None

    def move_up(self):
        self.origin.Y = self.origin.Y + 1
        self.extend(self.origin)
        return None

    def move_right(self):
        self.origin.X = self.origin.X + 1
        self.extend(self.origin)
        return None

    def move_bottom(self):
        self.origin.Y = self.origin.Y - 1
        self.extend(self.origin)
        return None


    def extend(self, point):
        point = Point(point.X, point.Y)
        self.trail.append(point)

    def getHousesCountVisitedOnceIncluding(self, otherTrail):
        totalTrail = self.trail
        totalTrail.extend(otherTrail)

        uniquePoints = []

        for point1 in totalTrail:
            found = False

            for point2 in uniquePoints:
                if point1.X == point2.X and point1.Y == point2.Y :
                    found = True

            if found == False:
                uniquePoints.append(point1)

        return len(uniquePoints)


def main():
    #
    # Entry point
    #
    trail = Trail('santa', 0, 0)
    trailRobot = Trail('robot', 0, 0)

    processingSanta = True
    with open('data.txt') as f:
        for c in f.read():

            # Toggle the trail every character
            if processingSanta == True :
                print "santa:" + c
                currentTrail = trail
            else:
                currentTrail = trailRobot
                print "robot:" + c


            if c == "<":
                currentTrail.move_left()
            elif c == "^":
                currentTrail.move_up()
            elif c == ">":
                currentTrail.move_right()
            elif c == "v":
                currentTrail.move_bottom()

            # Toggle trail switch flag
            processingSanta = not processingSanta

    print trail
    print trailRobot
    print "Number of houses visited once : " + str(trail.getHousesCountVisitedOnceIncluding(trailRobot.trail))


if __name__ == "__main__":
    main()
