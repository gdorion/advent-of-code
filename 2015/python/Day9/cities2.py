import re
import copy
import sys
import itertools

#London to Dublin = 464
#London to Belfast = 518
#Dublin to Belfast = 141

def findDistance(startCity, endCity, cityMap):
    for cityLink in cityMap:
        linkStart = cityLink[0]
        linkEnd = cityLink[1]
        if (startCity == linkStart and endCity == linkEnd) or (startCity == linkEnd and endCity == linkStart):
            return int(cityLink[2])

    return None


def computeDistance(path, cityMap):
    pathTotalDistance = 0
    for idx, city in enumerate(path):
        if idx+1 < len(path):
            pathTotalDistance = pathTotalDistance + findDistance(city, path[idx+1], cityMap)
    return pathTotalDistance


with open('data.txt') as f:
    data  = f.read().splitlines()
    city1    = map(lambda x: x.split(' ')[0], data)
    city2    = map(lambda x: x.split(' ')[2], data)
    distance = map(lambda x: x.split(' ')[4], data)

    content = []
    for i, e in enumerate(data):
        content.append([city1[i], city2[i], distance[i]])

    # Building unique list of cities.
    allCities = set()
    for link in content:
        allCities.add(link[0])
        allCities.add(link[1])

    paths = []

    currentPath = []

    allPossiblePaths = list(itertools.permutations(allCities))

    shortest = 0
    for path in allPossiblePaths:
        distance = computeDistance(path, content)
        if distance is not None:
            shortest = max(shortest, distance)
            print path

    print shortest

