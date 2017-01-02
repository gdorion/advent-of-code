#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com

building = {
    0: ["PRO_G", "PRO_C"],
    1: ["COB_G", "CUR_G", "RUT_G" "PLU_G"],
    2: ["COB_C", "CUR_C", "RUT_C" "PLU_C"],
    3: []
}

buildingTest = {
    0: ["HM", "LM"],
    1: ["HG"],
    2: ["LG"],
    3: []
}

optionCounts = []
elevator = 0

# backtrack !
def move(floorNo, items):
    global building
    global optionCounts

    if floorNo > 3:
        return False

    # LOGIC TO ADD HERE ....

    for item, i in enumerate(items):
        if i < len(items) - 1:
            result = move(floorNo+1, [item, items[i+1]])

# move(building, 0, ["PRO_G", "PRO_C"])
move(building, 0, ["HM", "LM"])
