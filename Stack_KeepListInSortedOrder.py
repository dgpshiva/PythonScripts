import math

def findDeliveries(numLocations, locations, numDeliveries):
    s1 = []
    s2 = []

    for location in locations:
        dist = math.sqrt( math.pow(location[0], 2) + math.pow(location[1], 2) )

        if len(s1) == 0:
            s1.append(dist)
        else:
            while len(s1) > 0 and dist > s1[len(s1) - 1]:
                s2.append(s1.pop())
            s1.append(dist)
            while len(s2) > 0:
                s1.append(s2.pop())


    result = []
    validDeliveries = numDeliveries if numDeliveries < len(s1) else len(s1)
    for i in range(0, validDeliveries):
        result.append(s1.pop())
    return result


if __name__ == '__main__':
    locations = [ [2, 2], [-1, 2], [2, 3] ]
    print findDeliveries(3, locations, 2)




