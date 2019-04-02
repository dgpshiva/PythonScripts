class JobExpiry():
    def __init__(self, unexpiredJobs):
        self.unexpiredJobs = unexpiredJobs
        self.rightExtremeIndex = len(self.unexpiredJobs)-1
        self.index = None

    def isExpired(self, jobID):
        leftExtreme = int(self.unexpiredJobs[0].split("-")[0]) if "-" in self.unexpiredJobs[0] else int(self.unexpiredJobs[0])
        if jobID < leftExtreme:
            return True
        
        rightExtreme = int(self.unexpiredJobs[self.rightExtremeIndex].split("-")[1]) if "-" in self.unexpiredJobs[self.rightExtremeIndex] else int(self.unexpiredJobs[self.rightExtremeIndex])
        if jobID > rightExtreme:
            return True
        
        return self.binarySearch(jobID)
    
    def expireJob(self, jobID):
        if not self.binarySearch(jobID):
            if "-" not in self.unexpiredJobs[self.index]:
                del self.unexpiredJobs[self.index]
            else:
                leftValue = int(self.unexpiredJobs[self.index].split("-")[0])
                rightValue = int(self.unexpiredJobs[self.index].split("-")[1])
                if jobID == leftValue:
                    del self.unexpiredJobs[self.index]
                    self.unexpiredJobs.insert(self.index, str(leftValue + 1) + "-" + str(rightValue))
                elif jobID == rightValue:
                    del self.unexpiredJobs[self.index]
                    self.unexpiredJobs.insert(self.index, str(leftValue) + "-" + str(rightValue - 1))
                elif jobID - leftValue == 1:
                    del self.unexpiredJobs[self.index]
                    self.unexpiredJobs.insert(self.index, str(jobID + 1) + "-" + str(rightValue))
                    self.unexpiredJobs.insert(self.index, str(leftValue))
                elif rightValue - jobID == 1:
                    del self.unexpiredJobs[self.index]
                    self.unexpiredJobs.insert(self.index, str(rightValue))
                    self.unexpiredJobs.insert(self.index, str(leftValue) + "-" + str(jobID - 1))
                else:
                    del self.unexpiredJobs[self.index]
                    self.unexpiredJobs.insert(self.index, str(jobID + 1) + "-" + str(rightValue))
                    self.unexpiredJobs.insert(self.index, str(leftValue) + "-" + str(jobID - 1))

            # Need to update right extreme after every successful expiry 
            # since the list changes
            self.rightExtremeIndex = len(self.unexpiredJobs) - 1
            return "Job expired"
        else:
            return "Job not found"
        
    def binarySearch(self, jobID):
        i = 0
        j = self.rightExtremeIndex

        while i<=j:
            mid = (i+j)//2

            if "-" not in self.unexpiredJobs[mid]:
                if jobID == int(self.unexpiredJobs[mid]):
                    self.index = mid
                    return False
                if jobID < int(self.unexpiredJobs[mid]):
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                leftValue = int(self.unexpiredJobs[mid].split("-")[0])
                rightValue = int(self.unexpiredJobs[mid].split("-")[1])
                if jobID >= leftValue and jobID <= rightValue:
                    self.index = mid
                    return False
                if jobID < leftValue:
                    j = mid - 1
                else:
                    i = mid + 1
            
        return True


if __name__ == '__main__':
    j = JobExpiry(["2", "100-150", "199", "200-210", "215", "300-350"])

    print j.unexpiredJobs
    print j.isExpired(349)
    print j.expireJob(349)
    print j.unexpiredJobs
    print j.isExpired(349)

    # print j.unexpiredJobs
    # print j.isExpired(348)
    # print j.expireJob(348)
    # print j.unexpiredJobs
    # print j.isExpired(348)

    # print j.unexpiredJobs
    # print j.isExpired(101)
    # print j.expireJob(101)
    # print j.unexpiredJobs
    # print j.isExpired(101)

    # print j.unexpiredJobs
    # print j.isExpired(1)
    # print j.expireJob(1)
    # print j.unexpiredJobs
    # print j.isExpired(1)

    # print j.unexpiredJobs
    # print j.isExpired(355)
    # print j.expireJob(355)
    # print j.unexpiredJobs
    # print j.isExpired(355)

    # print j.unexpiredJobs
    # print j.isExpired(2)
    # print j.expireJob(2)
    # print j.unexpiredJobs
    # print j.isExpired(2)

    # print j.unexpiredJobs
    # print j.isExpired(199)
    # print j.expireJob(199)
    # print j.unexpiredJobs
    # print j.isExpired(199)

    # print j.unexpiredJobs
    # print j.isExpired(3)
    # print j.expireJob(3)
    # print j.unexpiredJobs
    # print j.isExpired(3)

    # print j.unexpiredJobs
    # print j.isExpired(100)
    # print j.expireJob(100)
    # print j.unexpiredJobs
    # print j.isExpired(100)

    # print j.unexpiredJobs
    # print j.isExpired(150)
    # print j.expireJob(150)
    # print j.unexpiredJobs
    # print j.isExpired(150)









