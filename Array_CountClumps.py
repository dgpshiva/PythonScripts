# Given and array of elements, find the number of clumps in it.
# A clump is the same elements placed next to each other.
# Eg: [1, 2, 2, 3, 4, 4]    Ans: 2, one clump of 2, 2 and one of 4, 4

def countClumps(input):
    count = 0

    # Iterate over elements till n - 1
    for i in range(len(input) - 1):

        # If an element is equal to next element and 
        # not equal to previous element or current element's index is 0,
        # that marks start of a clump.
        if (input[i] == input[i+1]) and (i==0 or input[i] != input[i-1]):
            count += 1

    return count

if __name__ == '__main__':
    print countClumps([1, 2, 2, 3, 4, 4])   # Expectd output: 2
    print countClumps([1, 1, 2, 1, 1])  # Expectd output: 2
    print countClumps([1, 1, 1, 1, 1])  # Expectd output: 1
    print countClumps([1, 2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 3, 3])  # Expectd output: 1
    print countClumps([2, 3])  # Expectd output: 0
    print countClumps([2])  # Expectd output: 0
