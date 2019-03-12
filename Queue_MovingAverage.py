import Queue

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = Queue.Queue(maxsize = size)
        self.sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if not self.q.full():
            self.q.put(val)
            self.sum += val
            return self.sum/float(self.q.qsize())
        else:
            self.sum -= self.q.get()
            self.q.put(val)
            self.sum += val
            return self.sum/float(self.q.qsize())


if __name__ == '__main__':
    obj = MovingAverage(3)
    print obj.next(1)
    print obj.next(10)
    print obj.next(3)
    print obj.next(5)