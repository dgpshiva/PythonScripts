class SpecialStack:
    def __init__(self):
        self.s = []
        self.minVal = None

    def push(self, value):
        if len(self.s) == 0:
            self.s.append(value)
            self.minVal = value
        elif value < self.minVal:
            self.s.append(2*value - self.minVal)
            self.minVal = value
        else:
            self.s.append(value)

    def pop(self):
        if len(self.s) == 0:
            return "Stack is empty"
        value = self.s.pop()
        if value < self.minVal:
            toReturn = self.minVal
            self.minVal = 2*self.minVal - value
            return toReturn
        else:
            return value

    def getMin(self):
        return self.minVal

    def isEmpty(self):
        if len(self.s) == 0:
            return True


if __name__ == "__main__":
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
    print s.pop()
