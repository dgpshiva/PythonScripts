class SpecialStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, value):
        if len(self.s1) == len(self.s2) == 0:
            self.s1.append(value)
            self.s2.append(value)
        elif value > self.s2[len(self.s2) - 1]:
            self.s1.append(value)
        else:
            self.s1.append(value)
            self.s2.append(value)

    def pop(self):
        value = self.s1.pop()
        if value == self.s2[len(self.s2) - 1]:
            self.s2.pop()
        return value

    def getMin(self):
        return self.s2[len(self.s2) - 1]


if __name__ == '__main__':
    s = SpecialStack()
    s.push(18)
    s.push(19)
    s.push(29)
    s.push(15)
    s.push(16)

    print s.getMin()
    print s.pop()
    print s.getMin()
    print s.pop()
    print s.getMin()


