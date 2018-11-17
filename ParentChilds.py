# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   10

# Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one ancestor.

from collections import defaultdict

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10)
]

# Sample input and output:
# parent_child_pairs, 3, 8 => false
# parent_child_pairs, 5, 8 => true
# parent_child_pairs, 6, 8 => true


def returnIndividuals(parent_child_pairs, noParentIndividuals, oneParentIndividuals, input):
    keysSet = set()
    valuesSet = set()
    childParentDict = defaultdict(list)

    for pair in parent_child_pairs:
        keysSet.add(pair[0])
        valuesSet.add(pair[1])
        childParentDict[pair[1]].append(pair[0])

    for key in keysSet:
        if key not in valuesSet:
            noParentIndividuals.append(key)

    for k, v in childParentDict.iteritems():
        if len(v) == 1:
            oneParentIndividuals.append(k)


    firstValue = input[0]
    secondValue = input[1]

    firstValueAncs = []
    queue = []
    queue.append(firstValue)
    while len(queue) > 0:
        value = queue.pop()
        if value in childParentDict:
            firstValueAncs.extend(childParentDict[value])
            for parent in childParentDict[value]:
                queue.append(parent)

    secondValueAncs = []
    queue.append(secondValue)
    while len(queue) > 0:
        value = queue.pop()
        if value in childParentDict:
            secondValueAncs.extend(childParentDict[value])
            for parent in childParentDict[value]:
                queue.append(parent)

    for item in firstValueAncs:
        if item in secondValueAncs:
            return True
        else:
            pass
    return False



if __name__ == '__main__':
    noParentIndividuals = []
    oneParentIndividuals = []
    # input = (3, 8)
    # input = (5, 8)
    # input = (6, 8)
    input = (4, 8)
    print returnIndividuals(parent_child_pairs, noParentIndividuals, oneParentIndividuals, input)
    # print noParentIndividuals
    # print oneParentIndividuals
