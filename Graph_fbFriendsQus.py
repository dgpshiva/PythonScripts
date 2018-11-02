def countFriends(graph):
    result = {}
    for item in graph:
        for person in item:
            if person not in result:
                if len(item) == 1:
                    result[person] = 0
                else:
                    result[person] = 1
            else:
                result[person] = result[person] + 1

    return result

if __name__ == '__main__':
    graph = [['A','B'], ['A','C'], ['B','C'], ['E'], ['A', 'D']]
    print countFriends(graph)
