# You are given a truck of a given space.
# And packages that take a unique amount of space (no 2 packages will take the same amount of space).
# You have to fill the truck with exactly 2 packages and leave exactly 30 units of space.
# Find which 2 packages to select. 
# If more than one optimum combo take up the same amount of space, 
# return combo which has the heaviest package.

def IDsOfPackages(truckSpace, packagesSpace):
    # WRITE YOUR CODE HERE
    
    output = []
    if len(packagesSpace) < 2:
        return output
    
    if len(packagesSpace) == 2:
        return packagesSpace
    
    if truckSpace - 30 < 0:
        return output
    
    maxWeight = None
    weightIndex = {}
    
    for i in range(0, len(packagesSpace)):
        if truckSpace-30-packagesSpace[i] in weightIndex:
            if maxWeight is None or max(packagesSpace[i], truckSpace-30-packagesSpace[i]) > maxWeight:
                del output[:]
                maxWeight = max(packagesSpace[i], truckSpace-30-packagesSpace[i])
                output.append(i)
                output.append(weightIndex[truckSpace-30-packagesSpace[i]])
        weightIndex[packagesSpace[i]] = i

    return output
    
    
# print IDsOfPackages(110, [20, 70, 90, 30, 60, 110])
print IDsOfPackages(250, [100, 120, 180, 40, 10])