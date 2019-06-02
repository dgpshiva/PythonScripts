# You are given with a number of foreground running apps and background running apps
# with the amount of space they require to run.
# And a processor with max space it has.
# Need to find the best combination of foreground and background app that 
# can be run on the processor so that they utilize max space on the processor.
# If more than one optimum combo take up the same amount of space, output all such combos.

from collections import defaultdict

def optimalUtilization(deviceCapacity, foregroundAppsList, backgroundAppsList):
    # WRITE YOUR CODE HERE
    foregroundAppsSpaceSet = set()
    foregroundAppsSpaceList = []
    backgroundAppsSpaceSet = set()
    backgroundAppsSpaceList = []
    forgroundAppsSpaceIndex = defaultdict(list)
    backgroundAppsSpaceIndex = defaultdict(list)
    tempStack = []
    output = []
    
    if deviceCapacity <= 0:
        return output
    if len(foregroundAppsList) == 0 or len(backgroundAppsList) == 0:
        return [[]]
    
    for foregroundApp in foregroundAppsList:
        # App needs to be considered only if its space is less than device capacity
        if foregroundApp[1] < deviceCapacity:
            # Creating a list of unique foreground app spaces 
            # that always remains in sorted order
            if foregroundApp[1] not in foregroundAppsSpaceSet:
                foregroundAppsSpaceSet.add(foregroundApp[1])
                while len(foregroundAppsSpaceList) > 0 and foregroundAppsSpaceList[len(foregroundAppsSpaceList)-1] > foregroundApp[1]:
                    tempStack.append(foregroundAppsSpaceList.pop())
                foregroundAppsSpaceList.append(foregroundApp[1])
                while len(tempStack) > 0:
                    foregroundAppsSpaceList.append(tempStack.pop())
            # Add add space as key and its index to the value of hash map
            forgroundAppsSpaceIndex[foregroundApp[1]].append(foregroundApp[0])
        
    for backgroundApp in backgroundAppsList:
        # App needs to be considered only if its space is less than device capacity
        if backgroundApp[1] < deviceCapacity:
            # Creating a list of unique background app spaces 
            # that always remains in sorted order
            if backgroundApp[1] not in backgroundAppsSpaceSet:
                backgroundAppsSpaceSet.add(backgroundApp[1])
                while len(backgroundAppsSpaceList) > 0 and backgroundAppsSpaceList[len(backgroundAppsSpaceList)-1] > backgroundApp[1]:
                    tempStack.append(backgroundAppsSpaceList.pop())
                backgroundAppsSpaceList.append(backgroundApp[1])
                while len(tempStack) > 0:
                    backgroundAppsSpaceList.append(tempStack.pop())
            # Add add space as key and its index to the value of hash map
            backgroundAppsSpaceIndex[backgroundApp[1]].append(backgroundApp[0])
    
    minDifference = None
    for foregroundAppSpace in foregroundAppsSpaceList:
        closestBackgroundAppSpace = findClosest(backgroundAppsSpaceList, deviceCapacity - foregroundAppSpace)
        if closestBackgroundAppSpace is not None:
            if (minDifference is None) or (deviceCapacity - (foregroundAppSpace + closestBackgroundAppSpace) < minDifference):
                minDifference = deviceCapacity - (foregroundAppSpace + closestBackgroundAppSpace)
                del output[:]
                for foregroundAppIndex in forgroundAppsSpaceIndex[foregroundAppSpace]:
                    for backgroundAppIndex in backgroundAppsSpaceIndex[closestBackgroundAppSpace]:
                        output.append([foregroundAppIndex, backgroundAppIndex])
            elif deviceCapacity - (foregroundAppSpace + closestBackgroundAppSpace) == minDifference:
                for foregroundAppIndex in forgroundAppsSpaceIndex[foregroundAppSpace]:
                    for backgroundAppIndex in backgroundAppsSpaceIndex[closestBackgroundAppSpace]:
                        output.append([foregroundAppIndex, backgroundAppIndex])

    return output
    

# This function returns the closest smalled number to target 
# in the appSpaceList
def findClosest(appSpaceList, target):
    if target < appSpaceList[0]:
        return None
    elif target == appSpaceList[0]:
        return appSpaceList[0]

    if target >= appSpaceList[len(appSpaceList)-1]:
        return appSpaceList[len(appSpaceList)-1]
    
    i = 0 
    j = len(appSpaceList) - 1 
    while i < j:
        mid = (i + j)//2 
        if appSpaceList[mid] == target:
            return appSpaceList[mid]
        elif target < appSpaceList[mid]:
            if mid > 0 and target >= appSpaceList[mid-1]:
                return appSpaceList[mid-1]
            j = mid - 1
        else:
            if mid < len(appSpaceList) - 1 and target < appSpaceList[mid+1]:
                return appSpaceList[mid]
            i = mid + 1
    
    return None


deviceCapacity = 50
foregroundApps = [[1, 10], [2, 15], [3, 15], [4, 20], [5, 24], [6, 34], [7, 50]]
backgroundApps = [[1, 5], [2, 12], [3, 34], [4, 15], [5, 34], [6, 45]]
print optimalUtilization(deviceCapacity, foregroundApps, backgroundApps)