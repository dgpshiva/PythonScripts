def checkIfSumExists(input ,sum):
    s = set()
    for i in input:
        if sum-i>0 and sum-i in s:
            return True
        else:
            s.add(i)
    return False

if __name__ == '__main__':
    A = [1,4,45,6,10,8]
    # print checkIfSumExists(A, 51)
    print checkIfSumExists(A, 50)
