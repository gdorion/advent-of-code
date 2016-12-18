import math

class Point(object):
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def move_left(self):
        self.X = self.X - 1
        return None

    def move_up(self):
        self.Y = self.Y - 1
        return None

    def move_right(self):
        self.X = self.X + 1
        return None

    def move_bottom(self):
        self.Y = self.Y + 1
        return None


class Trail(object):
    def __init__(self):
        self.trail = []

    def extend(self, point):
        self.trail.append(point)
        print "Added : " + str(point)

    def getHousesCountVisitedOnce(self):
        uniquePoints = []
        for point1 in self.trail:
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
    origin = Point(0,0) # Where Santa starts it's run.
    trail = Trail() # The gifts delivery trail.
    trail.extend(origin)

    with open('data.txt') as f:
        for c in f.read():
            if c == "<":
                origin = Point(origin.X, origin.Y)
                origin.move_left()
                trail.extend(origin)
            elif c == "^":
                origin = Point(origin.X, origin.Y)
                origin.move_up()
                trail.extend(origin)
            elif c == ">":
                origin = Point(origin.X, origin.Y)
                origin.move_right()
                trail.extend(origin)
            elif c == "v":
                origin = Point(origin.X, origin.Y)
                origin.move_bottom()
                trail.extend(origin)


    print "Number of houses visited once : " + str(trail.getHousesCountVisitedOnce())

if __name__ == "__main__":
    main()

