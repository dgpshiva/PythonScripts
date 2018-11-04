import math

def reverse(input):
    characters = list(input)
    k = int(math.floor(len(characters)/2))
    for i in range(0, k):
        temp = characters[len(characters) -1 - i]
        characters[len(characters) -1 - i] = characters[i]
        characters[i] = temp

    return ''.join(characters)

if __name__ == '__main__':
    # input = "Nivi"
    # input = "Shiva"
    input = "This is a test"
    print reverse(input)
