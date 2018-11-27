import math

def checkIfPrime(input):
    if input <= 1:
        return False
    if input == 2:
        return True
    if input > 2 and input % 2 == 0:
        return False

    max_div = int(math.floor(math.sqrt(input)))
    for i in range(3, max_div+1, 2):
        if input % i == 0:
            return False
    return True


if __name__ == '__main__':
    # print checkIfPrime(13)
    print checkIfPrime(12)
