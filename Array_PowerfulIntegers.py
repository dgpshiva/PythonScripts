#Question: Return numbers <= bound which are equal to
# x^i + y^j
# where:
#   1 <= x <= 100
#   1 <= y <= 100
#   0 <= bound <= 10^6
#   i >= 0
#   j >= 0

import math

def returnPowerfulIntegers(x, y, bound):
    if bound == 0:
        return []

    output = []
    s = set()
    xs = [1] if x == 1 else [x**i for i in range(0, int(math.log(bound, x)+1))]
    ys = [1] if y == 1 else [y**j for j in range(0, int(math.log(bound, y)+1))]

    for i in xs:
        for j in ys:
            if i+j <= bound and i+j not in s:
                output.append(i+j)
                s.add(i+j)

    return output


if __name__ == '__main__':
    print returnPowerfulIntegers(2, 3, 10)
