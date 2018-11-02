import collections

# Without preserving order
# Fastest remove dups without preserving order
def removeDups(a):
    keys = {}
    for item in a:
        keys[item] = 1
    return keys.keys()

# Remove the value which has duplicates also
def removeValueWithDups(a):
    itemCount = {}
    result = []
    for item in a:
        if item not in itemCount:
            itemCount[item] = 1
        else:
            itemCount[item] += 1
    for key in itemCount:
        if itemCount[key] == 1:
            result.append(key)
    return result


# Preserving order
# Fastest remove dups preserving the order
# def removeDupsPreserveOrder(a, idfun = None):
#     if idfun is None:
#         def idfun(x) : return x
#     seen = {}
#     result = []
#     for item in a:
#         marker = idfun(item)
#         if marker in seen: continue
#         seen[marker] = 1
#         result.append(item)
#     return result

def removeDupsPreserveOrder(a):
    seen = {}
    result = []
    for item in a:
        if item in seen: continue
        seen[item] = 1
        result.append(item)
    return result

# Remove the value which has duplicates also
def removeValueWithDupsPreserveOrder(a):
    itemCount = collections.OrderedDict()
    result = []
    for item in a:
        if item not in itemCount:
            itemCount[item] = 1
        else:
            itemCount[item] += 1
    for key in itemCount:
        if itemCount[key] == 1:
            result.append(key)
    return result


if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 5, 1]

    # print removeDups(a)

    # print removeValueWithDups(a)

    # print removeDupsPreserveOrder(a)

    print removeValueWithDupsPreserveOrder(a)