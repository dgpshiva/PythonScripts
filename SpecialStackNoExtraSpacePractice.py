class SpecialStack:
    def __init__(self):
        self.s = []
        self.minEl = None

    def push(self, value):
        if len(self.s) == 0:
            self.s.append(value)
            self.minEl = value
        elif value < self.minEl:
            self.s.append(2*value - self.minEl)
            self.minEl = value
        else:
            self.s.append(value)

    def pop(self):
        if len(self.s) == 0:
            return None
        stackTop = self.s.pop()
        if stackTop <= self.minEl:
            toReturn = self.minEl
            self.minEl = 2*self.minEl - stackTop
            return toReturn
        else:
            return stackTop

    def getMin(self):
        return self.minEl


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


